def get_factors(n: int):
    return [num for num in range(1, n+1) if n % num == 0]

def hcf(a, b):
    return max(set(get_factors(a)).intersection(set(get_factors(b))))


def main():
    print(get_factors(1000))
    print(hcf(39547201236953378802969, 63988715761322450943144))


if __name__ == '__main__':
    main()

