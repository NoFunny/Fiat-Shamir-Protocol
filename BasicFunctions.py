import sys
import random
import math


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0:
        return False

    t, s = n - 1, 0

    while t % 2 == 0:
        t, s = t / 2, s + 1

    for i in range(0, k):
        a = random.randint(2, n - 2)
        x = fast_modulo_exponentiation(a, int(t), int(n))

        if x == 1 or x == n - 1:
            continue

        for r in range(1, s):
            x = fast_modulo_exponentiation(x, 2, n)

            if x == 1:
                return False

            if x == n - 1:
                break

        if x != n - 1:
            return False

    return True


def gen_p():
    p = random.randint(10 ** 6, 10 ** 9)

    while not (miller_rabin_test(p, int(math.log2(p))) and miller_rabin_test(p * 2 + 1, int(math.log2(p * 2 + 1)))):
        p = random.randint(10 ** 6, 10 ** 9)

    return 2 * p + 1


def gen_g(p):
    while True:
        g = random.randint(2, 100)
        if fast_modulo_exponentiation(g, int((p - 1) / 2), p) != 1 and is_prime(g):
            return g


def is_prime(n):
    if n <= 2:
        return False

    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0:
            return False

    return True


def mulinv(b, n):
    g, x, _ = genEuclideanAlgo(b, n)
    if g == 1:
        return x % n


def genEuclideanAlgo(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = genEuclideanAlgo(b % a, a)
        return g, y - (b // a) * x, x


def fast_modulo_exponentiation(a, x, p):
    if 1 > x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    result = 1
    tmp = a
    if a == 0:
        return 0
    if x < 0:
        tmp = mulinv(a, p)
        x = -x
    while x:
        if x & 1:
            result = (result * tmp) % p
        tmp = (tmp * tmp) % p
        x >>= 1
    return result
