def main():
    n = int(input())
    array = list(map(int, input().split()))

    for i in range(n // 2):
        array[i], array[n - i - 1] = array[n - i - 1], array[i]

    print(" ".join([str(el) for el in array]))


if __name__ == '__main__':
    main()
