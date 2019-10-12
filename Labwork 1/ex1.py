def maj(x, y, z):
    return 0 if x + y + z < 2 else 1


def mod2(x):
    return 1 if x % 2 == 1 else 0


def a5(X, Y, Z):
    output = mod2(X[18] + Y[21] + Z[22])
    m = maj(X[8], Y[10], Z[10])
    if X[8] == m:
        first = mod2(X[13] + X[16] + X[17] + X[18])
        X[1:19] = X[0:18]
        X[0] = first
    if Y[10] == m:
        first = mod2(Y[20] + Y[21])
        Y[1:22] = Y[0:23]
        Y[0] = first
    if Z[10] == m:
        first = mod2(Z[20] + Z[21] + Z[22])
        Z[1:23] = Z[0:22]
        Z[0] = first
    return output


X = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Y = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
Z = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
for i in range(10):
    print(a5(X, Y, Z), end='')
