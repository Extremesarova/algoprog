def main():
    even_count = 0
    num = int(input())
    while num != 0:
        even_count += 1 if num % 2 == 0 else 0
        num = int(input())
    print(even_count)


if __name__ == '__main__':
    main()
