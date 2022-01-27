"""
Author:Maola Sirzul
Date created: 26/01/2021
Version:1.0
Description:5. Is prime?
"""

import time


def is_prime(n):
    if n < 1:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True


# Driver function

t0 = time.time()

c = 0  # for counting

for n in range(1, 1000):
    x = is_prime(n)

    c += x

print("Total prime numbers in range :", c)

t1 = time.time()

print("Time required :", t1 - t0)