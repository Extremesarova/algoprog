def get_first_digit(num):
    return int(num * 10) % 10


def main():
    num = float(input())
    first_digit = get_first_digit(num)
    print(first_digit)

    # assert get_first_digit(1.79) == 7
    # assert get_first_digit(1234.5678) == 5
    # assert get_first_digit(1.01) == 0


if __name__ == '__main__':
    main()
