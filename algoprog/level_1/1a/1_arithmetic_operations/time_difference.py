def main():
    h1, m1, s1 = int(input()), int(input()), int(input())
    h2, m2, s2 = int(input()), int(input()), int(input())
    time_difference = (h2 - h1) * 60 * 60 + (m2 - m1) * 60 + (s2 - s1)

    print(time_difference)


if __name__ == '__main__':
    main()
