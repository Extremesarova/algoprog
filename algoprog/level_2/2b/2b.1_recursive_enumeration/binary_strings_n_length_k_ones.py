def find(a, n, k):
    def check(a):
        if a.count(1) == k:
            print("".join(map(str, a)))

    def find_rec(i):
        if i == n:
            check(a)
            return

        if k - a[:i].count(1) > n - i:
            return

        for j in range(2):
            a[i] = j
            find_rec(i + 1)
            if a[: i + 1].count(1) == k:
                return

    find_rec(0)


def main():
    n, k = map(int, input().split())
    a = [None] * n

    find(a, n, k)


if __name__ == '__main__':
    main()
