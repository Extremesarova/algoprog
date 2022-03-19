def get_string(n):
    letters = "ABCDEF"
    if n == 1:
        return "A"
    else:
        return get_string(n - 1) + letters[n - 1] + get_string(n - 1)


def main():
    n = int(input())
    str_ = get_string(n)

    print(str_)

    # assert get_string(1) == "A"
    # assert get_string(2) == "ABA"
    # assert get_string(3) == "ABACABA"


if __name__ == '__main__':
    main()
