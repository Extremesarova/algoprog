def main():
    n = int(input())
    res = "NO"
    for _ in range(0, n):
        num = int(input())
        if num == 0:
            res = "YES"
            break
    print(res)


if __name__ == '__main__':
    main()
