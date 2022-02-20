def get_pupils(n, k):
    left_apples = k % n
    pupils = (n - left_apples) % n
    return pupils


def main():
    n = int(input())
    k = int(input())

    pupils = get_pupils(n, k)
    print(pupils)

    assert get_pupils(7, 30) == 5
    assert get_pupils(7, 28) == 0
    assert get_pupils(7, 35) == 0
    assert get_pupils(7, 34) == 1


if __name__ == '__main__':
    main()
