# elgalma digital signature
from square_and_multiply import square_and_multiply
from dsa import mulinv


def eds(p, alpha, d, ke, x):
    beta = square_and_multiply(alpha, d, p)
    r = square_and_multiply(alpha, ke, p)
    s = ((x - d * r) % (p - 1) * mulinv(ke, p - 1)) % (p - 1)
    t = square_and_multiply(beta, r, p) * square_and_multiply(r, s, p) % p
    if t == square_and_multiply(alpha, x, p):
        print("the signature is verified")
    else:
        print("there is something wrong")
    print("beta =", beta)
    print("r =", r)
    print("s =", s)
    print("t =", t)
    print("the public keys are p =", p, ", alpha =", alpha,", beta =", beta)
    print("the private keys is d =", d)


eds(467, 2, 127, 213, 1601)