def fib(n):
    fib_array = [1, 1]
    for i in range(2, n):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    return fib_array[n - 1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
