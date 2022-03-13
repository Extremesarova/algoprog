def get_gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x


def reduce_fraction(a, b):
    gcd = get_gcd(a, b)
    c = a // gcd
    d = b // gcd

    return c, d


def main():
    a, b = map(int, input().split())

    c, d = reduce_fraction(a, b)
    print(c, d)

    assert reduce_fraction(3, 6) == (1, 2)
    assert reduce_fraction(20, 15) == (4, 3)
    assert reduce_fraction(-2, 5) == (-2, 5)
    assert reduce_fraction(-5, 10) == (-1, 2)


if __name__ == '__main__':
    main()
