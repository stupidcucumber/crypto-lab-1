from typing import Iterator
from .millerrabin import miller_rabin_test


def _jacobi(a: int, n: int) -> int:
    if n <= 0 or not n & 1:
        raise ValueError('n must be greater than zero and must be an odd.')
    a = a % n
    t = 1
    r = 0
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        r = n
        n = a
        a = r
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a = a % n
    if n == 1:
        return t
    return 0


def sequence() -> Iterator[int]:
    start = 5
    step = 0
    while True:
        yield start * ((-1) ** step)
        start += 2
        step += 1


def baillie_psw_test(number: int) -> bool:
    if not number & 1:
        return False
    if not miller_rabin_test(number=number):
        return False

    for element in sequence():
        if _jacobi(element, number) == -1:
            D = element
            break
    
    P = 1
    Q = (1 - D) / 4
    