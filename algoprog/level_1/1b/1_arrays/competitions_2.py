def main():
    arr = []
    n, m = map(int, input().split())
    for i in range(n):
        arr.append(list(map(int, input().split())))

    max_el = arr[0][0]
    el_row = 0
    el_col = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] > max_el:
                max_el = arr[i][j]
                el_row = i
                el_col = j
    print(max_el)
    print(el_row, el_col)


if __name__ == '__main__':
    main()
