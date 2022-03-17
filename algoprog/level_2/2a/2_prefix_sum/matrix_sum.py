def get_prefix_array_matrix(a):
    num_rows = len(a) + 1
    num_cols = len(a[0]) + 1
    prefix_array = [[0 for x in range(num_cols)] for y in range(num_rows)]
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            prefix_array[i][j] = a[i - 1][j - 1] \
                                 + prefix_array[i - 1][j] \
                                 + prefix_array[i][j - 1] \
                                 - prefix_array[i - 1][j - 1]

    return prefix_array


def get_range_sum_inclusively(prefix_array, x1, y1, x2, y2):
    return prefix_array[x2][y2] \
           - prefix_array[x1 - 1][y2] \
           - prefix_array[x2][y1 - 1] \
           + prefix_array[x1 - 1][y1 - 1]


def main():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    pref = get_prefix_array_matrix(a)

    x_y_tuple_list = []
    for _ in range(k):
        x_y_tuple_list.append(tuple(map(int, input().split())))

    for (x1, y1, x2, y2) in x_y_tuple_list:
        print(get_range_sum_inclusively(pref, x1, y1, x2, y2))

    # assert get_range_sum_inclusively(a, 2, 2, 3, 3) == 28
    # assert get_range_sum_inclusively(a, 1, 1, 2, 3) == 31


if __name__ == '__main__':
    main()
