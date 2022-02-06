def main():
    h = float(input())
    m = float(input())
    s = float(input())

    # there is 60 * 60 seconds in one hour, and it's equal to 360 / 12 degrees
    # we are going to find how many seconds it takes to reach one degree

    divider = (60 * 60) / (360 / 12)
    overall_s = h * 60 * 60 + m * 60 + s
    result = overall_s / divider

    print(result)


if __name__ == '__main__':
    main()
