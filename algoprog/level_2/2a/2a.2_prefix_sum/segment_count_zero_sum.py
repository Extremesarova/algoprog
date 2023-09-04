# https://www.youtube.com/watch?v=de28y8Dcvkg

def count_zero_sum_ranges_3(a):
    # Time: O(n^3)
    n = len(a)
    ranges_counter = 0

    for l in range(n):
        for r in range(l + 1, n + 1):
            range_sum = 0
            for k in range(l, r):
                range_sum += a[k]
            if range_sum == 0:
                ranges_counter += 1

    return ranges_counter


def count_zero_sum_ranges_2(a):
    # Time: O(n^2)
    n = len(a)
    ranges_counter = 0

    for l in range(n):
        range_sum = 0
        for r in range(l, n):
            range_sum += a[r]

            if range_sum == 0:
                ranges_counter += 1

    return ranges_counter


def count_zero_sum_ranges(a):
    # Time: O(n)
    current_sum = 0
    ranges_counter = 0
    prefix_sum_by_value = {0: 1}

    for el in a:
        current_sum += el
        if current_sum not in prefix_sum_by_value:
            prefix_sum_by_value[current_sum] = 0
        ranges_counter += prefix_sum_by_value[current_sum]
        prefix_sum_by_value[current_sum] += 1

    return ranges_counter


def main():
    a = [-1, -2, 1, 2, 3, 4, -1, -1, -2, 1, 10, 12, 4, 5, 6, -9, -6, -1, -2, 1, 2, 3, 4, -1, -1, -2, 1, 10, 12, 4, 5, 6, -9, -6]

    assert count_zero_sum_ranges_3(a) == 9
    assert count_zero_sum_ranges_2(a) == 9
    assert count_zero_sum_ranges(a) == 9


if __name__ == "__main__":
    main()
