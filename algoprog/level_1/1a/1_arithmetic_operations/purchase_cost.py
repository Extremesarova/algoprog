def main():
    a, b, n = int(input()), int(input()), int(input())
    rubles = a * n + b * n // 100
    cents = b * n % 100

    print(rubles, cents)


if __name__ == '__main__':
    main()
