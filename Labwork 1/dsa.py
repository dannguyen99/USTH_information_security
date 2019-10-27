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


def signature(hx, p, q, alpha, d, ke):
    beta = square_and_multiply(alpha, d, p)
    r = square_and_multiply(square_and_multiply(alpha, ke, p), 1, q)
    s = square_and_multiply((hx + d * r) * mulinv(ke, q), 1, q)
    w = mulinv(s, q) % q
    u1 = w * hx % q
    u2 = w * r % q
    v = square_and_multiply(
        square_and_multiply(square_and_multiply(alpha, u1, p) * square_and_multiply(beta, u2, p), 1, p), 1, q)
    print("beta = ", beta)
    print("r = ", r)
    print("s = ", s)
    print("w = ", w)
    print("u1 = ", u1)
    print("u2 = ", u2)
    print("v = ", v)
    if v == r % q:
        print("the signature is valid")
    else:
        print("invalid, please recompute")


signature(26, 59, 29, 3, 7, 10)
st = "abc"
print(' '.join(format(ord(x), 'b') for x in st))