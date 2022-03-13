def main():
    x, y = map(float, input().split())

    counter = 1
    mult = 0.7
    eps = 10e-8

    while y > x + eps:
        x += x * mult
        counter += 1

    print(counter)


if __name__ == '__main__':
    main()
