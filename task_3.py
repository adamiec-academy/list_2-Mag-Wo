def is_prime(n):
        if n < 2:
        return False
    for i in (2,(n-1)):
        if (n % i) == 0:
            return False
    return True


def is_diabolic(n):
    return "666" in str(n)


def final(n):

    for i in range (100000):
        if is_diabolic(i) and is_prime(i):
            print(i)
     
