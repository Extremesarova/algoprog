def check(a):
    print("".join(map(str, a)))


def find(a, k):
    def find_rec(i):
        if i == k:
            check(a)
            return
        a[i] = 0
        find_rec(i + 1)
        a[i] = 1
        find_rec(i + 1)

    find_rec(0)


def main():
    n = int(input())
    a = [None] * n

    find(a, n)


if __name__ == '__main__':
    main()
