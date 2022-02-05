def main():
    n = int(input())
    sum_squares = sum([num ** 2 for num in range(1, n + 1)])

    print(sum_squares)


if __name__ == '__main__':
    main()
