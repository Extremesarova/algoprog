def main():
    n = int(input())
    arr = list(map(int, input().split()))

    future_zero_el = arr[n - 1]
    for i in range(n - 1, -1, -1):
        arr[i] = arr[i - 1]
    arr[0] = future_zero_el

    print(" ".join([str(el) for el in arr]))


if __name__ == '__main__':
    main()
