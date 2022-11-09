def is_prime(n):
    if n <= 1:
        return False
    for i in (2, n):
        if n % i == 0:
            return False
        else:
            return True


def is_diabolic(n):
    if "666" in str(n):
        return True


def final(n):
    a = 0
    for i in range (1,100000):
        if is_diabolic(i) and is_prime(i):
            return i  

            a += 1

final(100000)
