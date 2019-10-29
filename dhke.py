from square_and_multiply import square_and_multiply


# diffie-hellman key exchange
def dhke(p, alpha, a, b):
    A = square_and_multiply(alpha, a, p)
    B = square_and_multiply(alpha, b, p)
    key = square_and_multiply(A, b, p)
    print("public keys are:", A, "and", B)
    print("common private key is:", key)
    return key


dhke(467, 2, 400, 57)
