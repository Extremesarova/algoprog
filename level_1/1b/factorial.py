def main():
    n = int(input())

    s = 1
    sum_term = 1 / 1

    for i in range(1, n + 1):
        sum_term *= 1/i
        s += sum_term

    print(s)


if __name__ == '__main__':
    main()
