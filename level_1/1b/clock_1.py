def main():
    h = float(input())
    m = float(input())
    s = float(input())

    overall_s = h * 60 * 60 + m * 60 + s
    result = overall_s / 120

    print(result)


if __name__ == '__main__':
    main()
