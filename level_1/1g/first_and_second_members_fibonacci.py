def get_first_and_second_members(n, an, an_plus_one):
    x = [an_plus_one, an]
    for i in range(n - 1):
        x.append(x[i] - x[i + 1])

    return x[-2:][::-1]


def main():
    n = int(input())
    an, an_plus_one = map(int, input().split())

    members = get_first_and_second_members(n, an, an_plus_one)
    print(*members)

    # assert get_first_and_second_members(4, 3, 5) == [1, 1]
    # assert get_first_and_second_members(6, 31, 50) == [2, 5]
    # assert get_first_and_second_members(4, -12, -19) == [-2, -5]


if __name__ == '__main__':
    main()
