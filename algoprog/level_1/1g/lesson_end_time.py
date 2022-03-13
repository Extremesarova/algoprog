def get_lesson_end_time(n):
    lesson_length = 45
    odd_lesson_break = 5
    even_lesson_break = 15
    start_of_the_day = 9 * 60

    num_odd_breaks = n // 2
    num_even_breaks = n // 2 if n % 2 != 0 else n // 2 - 1
    lesson_end_time = (
            start_of_the_day
            + n * lesson_length
            + num_even_breaks * even_lesson_break
            + num_odd_breaks * odd_lesson_break
    )

    hour = lesson_end_time // 60
    minutes = lesson_end_time % 60

    return hour, minutes


def main():
    n = int(input())

    lesson_end_time = get_lesson_end_time(n)
    print(*lesson_end_time)

    assert get_lesson_end_time(3) == (11, 35)


if __name__ == '__main__':
    main()
