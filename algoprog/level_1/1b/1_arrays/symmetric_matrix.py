def main():
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int, input().split())))

    res = 'yes'
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                res = 'no'
                break
    print(res)


if __name__ == '__main__':
    main()
