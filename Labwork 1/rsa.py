def to_bin(x):
    output = bin(x)[2:]
    return output[::-1]


def square_and_multiply(base, power, mod):
    before = base % mod
    mod_value = [before]
    number_iter = len(to_bin(power))
    result = 1
    for i in range(number_iter - 1):
        before = (before * before) % mod
        mod_value.append(before)
    for i in range(number_iter):
        if int(to_bin(power)[i]) == 1:
            result *= mod_value[i]
            result %= mod
    return result


def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, b)
    if g == 1:
        return x % b


def gcd(a, b):
    if a == 0:
        return a
    if b == 0:
        return b
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def lcm(a, b):
    return (abs(a * b)) / gcd(a, b)


def rsa(p, q, e, M, option="encrypt"):
    n = p * q
    if option == "encrypt":
        return square_and_multiply(M, e, n)
    else:
        ctf = int(lcm((p - 1), (q - 1)))
        d = mulinv(e, int(ctf))
        return square_and_multiply(M, d, n)


print(rsa(5, 17, 3, 29,'encrypt'))
print(mulinv(10, 29))