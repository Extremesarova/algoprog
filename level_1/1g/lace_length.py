def get_lace_length(a, b, l, n):
    return 2 * l + 2 * (n - 1) * (a + b) + a


def main():
    a = int(input())
    b = int(input())
    l = int(input())
    n = int(input())

    lace_length = get_lace_length(a, b, l, n)
    print(lace_length)

    assert get_lace_length(2, 1, 3, 4) == 26


if __name__ == '__main__':
    main()
