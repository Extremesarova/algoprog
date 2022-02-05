def main():
    n = int(input())
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    print(divisor)


if __name__ == '__main__':
    main()
