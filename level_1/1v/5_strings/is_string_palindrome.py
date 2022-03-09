def is_string_palindrome(s):
    is_palindrome = 'yes'
    string_length = len(s)
    for i in range(string_length // 2):
        if s[i] != s[string_length - 1 - i]:
            is_palindrome = 'no'
            break
    return is_palindrome


def main():
    s = ''.join(input().split())
    is_palindrome = is_string_palindrome(s)
    print(is_palindrome)

    # assert is_string_palindrome("".join('king       are  you glad     you  are   king'.split())) == 'no'
    # assert is_string_palindrome("".join('was it a car or a cat i saw'.split())) == 'yes'
    # assert is_string_palindrome("".join('mom'.split())) == 'yes'
    # assert is_string_palindrome("".join('granddad'.split())) == 'no'


if __name__ == '__main__':
    main()
