def get_prefix_array(a):
    length = len(a)
    prefix_count_zero = [0] * (length + 1)
    cum_counter = 0

    for i in range(1, length + 1):
        cum_counter += 1 if a[i - 1] == 0 else 0
        prefix_count_zero[i] = cum_counter

    return prefix_count_zero


def get_zero_counts(prefix_array, left, right):
    return prefix_array[right] - prefix_array[left - 1]


def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    prefix_count_zero = get_prefix_array(a)

    l_r_tuple_list = []
    for _ in range(k):
        l_r_tuple_list.append(tuple(map(int, input().split())))

    for (l, r) in l_r_tuple_list:
        print(get_zero_counts(prefix_count_zero, l, r))

    # assert get_prefix_array([0, 0, 0, 0, 2]) == [0, 1, 2, 3, 4, 4]
    # assert get_zero_counts(get_prefix_array([0, 0, 0, 0, 2]), 2, 3) == 2
    # assert get_zero_counts(get_prefix_array([0, 0, 0, 0, 2]), 2, 5) == 3
    # assert get_zero_counts(get_prefix_array([0, 0, 0, 0, 2]), 1, 5) == 4
    # assert get_zero_counts(get_prefix_array([0, 0, 0, 0, 2]), 4, 5) == 1


if __name__ == '__main__':
    main()
