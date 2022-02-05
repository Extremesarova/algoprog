def main():
    word = input()

    is_palindrome = 'yes' if word == word[::-1] else 'no'

    print(is_palindrome)


if __name__ == '__main__':
    main()
