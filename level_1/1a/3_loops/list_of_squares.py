def main():
    n = int(input())
    num = 1
    while num ** 2 <= n:
        print(num ** 2, end=" ")
        num += 1


if __name__ == '__main__':
    main()
