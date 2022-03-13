def main():
    n = int(input())
    array = list(map(int, input().split()))

    counter = 0
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
