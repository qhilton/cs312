import math
import random
import sys
from time import time


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N


def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    for i in range(0, k):
        if (mod_exp(random.randint(1,N-1), N-1, N) % N != 1):
            return False
    return True


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """

    u = N-1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1

    if N < 2:
        return False
    if N in (2, 3):
        return True
    if N % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, N - 2)

        current = mod_exp(a, u, N)

        if current == 1 or current == N - 1:
            continue

        for _ in range(t - 1):
            current = mod_exp(current, 2, N)
            if current == N - 1:
                break
        else:
            return False

    return True


def generate_large_prime(n_bits: int) -> int:
    """Generate a random prime number with the specified bit length"""
    prime: bool = False
    bits: int
    k = 20
    while not prime:
        bits =  random.getrandbits(n_bits)
        prime = fermat(bits, k)
    return bits  # https://xkcd.com/221/


def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
