def main():
    a = int(input())
    b = int(input())

    if a > b:
        max_num = 1
    elif b > a:
        max_num = 2
    else:
        max_num = 0

    print(max_num)


if __name__ == '__main__':
    main()
