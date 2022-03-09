def main():
    x = int(input())

    if x > 0:
        sign = 1
    elif x < 0:
        sign = -1
    else:
        sign = 0

    print(sign)


if __name__ == '__main__':
    main()
