def main():
    char = input()

    is_digit = 'yes' if 48 <= ord(char) <= 57 else 'no'

    print(is_digit)


if __name__ == '__main__':
    main()
