def exponentiation_by_squaring(x, n):
    if n < 0:
        return exponentiation_by_squaring(1/x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exponentiation_by_squaring(x*x, n/2)
    else:
        return exponentiation_by_squaring(x*x, (n-1)/2)


print(exponentiation_by_squaring(6, 70) % 11)