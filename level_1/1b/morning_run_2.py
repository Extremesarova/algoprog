def main():
    first_row = input().split()
    if len(first_row) == 2:
        x, y = map(float, first_row)
    else:
        x = float(first_row[0])
        y = float(input())

    counter = 1
    mult = 0.7
    eps = 10e-8
    acc_x = x

    while y > acc_x + eps:
        x += x * mult
        acc_x += x
        counter += 1

    print(counter)


if __name__ == '__main__':
    main()
