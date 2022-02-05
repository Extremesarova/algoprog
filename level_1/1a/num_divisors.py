def main():
    n = int(input())
    num_divisors = [str(num) for num in range(1, n + 1) if n % num == 0]

    print(" ".join(num_divisors))


if __name__ == '__main__':
    main()
