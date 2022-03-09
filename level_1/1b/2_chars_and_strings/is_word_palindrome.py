def main():
    word = input()

    is_palindrome = 'yes'
    word_length = len(word)

    for i in range(word_length // 2):
        if word[i] != word[word_length - 1 - i]:
            is_palindrome = 'no'
            break

    print(is_palindrome)


if __name__ == '__main__':
    main()
