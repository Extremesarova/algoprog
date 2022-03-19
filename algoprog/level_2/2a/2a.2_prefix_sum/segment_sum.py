def get_prefix_array(a):
    length = len(a)
    prefix_sum = [0] * (length + 1)

    for i in range(1, length + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    return prefix_sum


def get_range_sum_inclusively(prefix_array, left, right):
    return prefix_array[right] - prefix_array[left - 1]


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    prefix_sum = get_prefix_array(a)

    x_y_tuple_list = []
    for _ in range(m):
        x_y_tuple_list.append(tuple(map(int, input().split())))

    for (x, y) in x_y_tuple_list:
        print(get_range_sum_inclusively(prefix_sum, x, y))

    # assert get_prefix_array(a) == [0, 1, 3, 6, 10, 15]
    # assert get_range_sum_inclusively(prefix_sum, 1, 5) == 15
    # assert get_range_sum_inclusively(prefix_sum, 2, 4) == 9
    # assert get_range_sum_inclusively(prefix_sum, 3, 5) == 12
    # assert get_range_sum_inclusively(prefix_sum, 1, 2) == 3


if __name__ == '__main__':
    main()
