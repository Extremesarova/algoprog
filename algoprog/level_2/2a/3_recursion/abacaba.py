import matplotlib.pyplot as plt


def get_string(n):
    letters = "ABCDEF"
    if n == 1:
        return "A"
    else:
        return get_string(n - 1) + letters[n - 1] + get_string(n - 1)


def main():
    n = int(input())
    str_ = get_string(n)

    print(str_)

    # assert get_string(1) == "A"
    # assert get_string(2) == "ABA"
    # assert get_string(3) == "ABACABA"


if __name__ == '__main__':
    main()

x1, y1, x2, y2 = 0, 0, 6, 4
x1, y1, x2, y2 = 3, 3, -3, 3
plt.plot((x1, x2), (y1, y2))
plt.grid(True)
plt.axis('equal')
