def main():
    char = input()

    char_code = ord(char)
    difference = ord('a') - ord('A')
    upper_char = chr(char_code - difference) if 'a' <= char <= 'z' else char

    print(upper_char)


if __name__ == '__main__':
    main()
