def get_gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return get_gcd_rec(b, a % b)


def main():
    a, b = map(int, input().split())

    gcd = get_gcd_rec(a, b)

    print(gcd)

    # assert get_gcd_rec(2, 1) == 1
    # assert get_gcd_rec(1, 2) == 1
    # assert get_gcd_rec(5, 3) == 1
    # assert get_gcd_rec(5, 10) == 5


if __name__ == '__main__':
    main()
