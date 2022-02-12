def main():
    n = int(input())
    arr = map(int, input().split())

    max_value = -1000
    for val in arr:
        if val > max_value:
            max_value = val

    print(max_value)


if __name__ == '__main__':
    main()
