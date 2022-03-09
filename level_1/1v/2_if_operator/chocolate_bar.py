def main():
    n = int(input())
    m = int(input())
    k = int(input())

    left = n * m - k

    if (left % n == 0 or left % m == 0) and left > 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
