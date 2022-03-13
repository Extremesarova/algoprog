def main():
    a = int(input())
    b = int(input())
    c = int(input())

    max_ab = b if b > a else a
    max_abc = c if c > max_ab else max_ab

    print(max_abc)


if __name__ == '__main__':
    main()
