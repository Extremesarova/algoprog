def main():
    n = int(input())
    counter = 0

    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
            counter += 1
            if counter == n:
                break
        if counter == n:
            break


if __name__ == '__main__':
    main()
