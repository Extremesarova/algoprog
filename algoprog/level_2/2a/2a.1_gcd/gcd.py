def get_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def main():
    x, y = map(int, input().split())

    gcd = get_gcd(x, y)
    print(gcd)

    # assert get_gcd(1, 1) == 1
    # assert get_gcd(2, 1) == 1
    # assert get_gcd(1, 2) == 1
    # assert get_gcd(5, 3) == 1
    # assert get_gcd(5, 10) == 5
    # assert get_gcd(10, 5) == 5


if __name__ == '__main__':
    main()
