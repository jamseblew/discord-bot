from math import sqrt, floor

def is_prime(n: int):
    if n < 2:
        return False

    for denom in range(2, int(sqrt(n))+1):
        if n % denom == 0:
            return False
    return True


def get_primes(n: int):
    return [num for num in range(1, n+1) if is_prime(num)]


def main():
    print(get_primes(1000))
    print(is_prime(27))
    print(is_prime(59))

if __name__ == '__main__':
    main()


