def main():
    a = float(input())
    b = float(input())
    c = float(input())

    eps = 1e-10

    result = "YES" if abs(a + b - c) < eps else "NO"

    print(result)


if __name__ == '__main__':
    main()
