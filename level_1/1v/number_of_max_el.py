def main():
    max_val = - 1
    max_count = 0

    val = int(input())

    while val != 0:
        if val > max_val:
            max_val = val
            max_count = 1
        elif val == max_val:
            max_count += 1

        val = int(input())

    print(max_count)


if __name__ == '__main__':
    main()
