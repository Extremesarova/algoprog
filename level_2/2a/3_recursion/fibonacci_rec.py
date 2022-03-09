def get_fib(n):
    if n <= 1:
        return n
    else:
        return get_fib(n - 1) + get_fib(n - 2)


def main():
    n = int(input())

    fib_n = get_fib(n)

    print(fib_n)

    # assert get_fib(0) == 0
    # assert get_fib(1) == 1
    # assert get_fib(2) == 1
    # assert get_fib(6) == 8
    # assert get_fib(9) == 34


if __name__ == '__main__':
    main()
