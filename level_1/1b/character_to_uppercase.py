def main():
    char = input()

    char_code = ord(char)

    upper_char = chr(char_code - 32) if 97 <= char_code <= 122 else char

    print(upper_char)


if __name__ == '__main__':
    main()
