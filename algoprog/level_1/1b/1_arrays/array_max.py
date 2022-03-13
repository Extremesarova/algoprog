def main():
    n = int(input())
    arr = list(map(int, input().split()))

    max_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el

    print(max_el)


if __name__ == '__main__':
    main()
