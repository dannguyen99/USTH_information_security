def to_bin(x):
    output = bin(x)[2:]
    return output[::-1]


def to_dec(x):
    return int(x, 2)


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


print(square_and_multiply(20*29,1, 59))
