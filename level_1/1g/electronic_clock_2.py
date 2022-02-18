def get_time(seconds_init):
    seconds_in_hour = 60 * 60
    minutes_in_hour = 60
    hours_in_day = 24

    hours_full = seconds_init // seconds_in_hour
    hours = hours_full % hours_in_day

    seconds_left = (seconds_init - hours_full * seconds_in_hour)

    minutes = seconds_left // minutes_in_hour
    seconds = (seconds_left - minutes * minutes_in_hour)

    time = f"{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return time


def main():
    seconds_initial = int(input())
    time = get_time(seconds_initial)
    print(time)

    # assert get_time(3602) == "1:00:02"
    # assert get_time(129700) == "12:01:40"


if __name__ == '__main__':
    main()
