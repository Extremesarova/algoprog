def main():
    n = int(input())
    n_factorial = 1
    for num in range(1, n + 1):
        n_factorial *= num

    print(n_factorial)


if __name__ == '__main__':
    main()
