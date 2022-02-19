def get_time(seconds_init):
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    hours_in_day = 24

    hours_full = seconds_init // seconds_in_hour
    hours = hours_full % hours_in_day

    seconds_left = seconds_init % seconds_in_hour

    minutes = seconds_left // seconds_in_minute
    seconds = seconds_left % seconds_in_minute

    time = f"{hours}:{minutes // 10}{minutes % 10}:{seconds // 10}{seconds % 10}"
    return time


def main():
    seconds_initial = int(input())
    time = get_time(seconds_initial)
    print(time)

    # assert get_time(3602) == "1:00:02"
    # assert get_time(129700) == "12:01:40"


if __name__ == '__main__':
    main()
