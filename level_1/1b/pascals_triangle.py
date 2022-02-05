def main():
    arr = []
    n, m = map(int, input().split())

    for i in range(n):
        arr.append([0] * m)
        arr[i][0] = 1

    for i in range(m):
        arr[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]

    print("\n".join([" ".join([str(el) for el in row]) for row in arr]))


if __name__ == '__main__':
    main()
