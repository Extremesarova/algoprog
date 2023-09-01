def get_day(h, a, b):
    counter = 0
    while True:
        counter += 1
        h -= a
        if h <= 0:
            return counter
        h += b


def main():
    # h = int(input())
    # a = int(input())
    # b = int(input())
    # day = get_day(h, a, b)
    # print(day)

    assert get_day(10, 3, 2) == 8


if __name__ == "__main__":
    main()
