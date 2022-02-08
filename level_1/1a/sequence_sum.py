def main():
    sequence_sum = 0
    while True:
        num = int(input())
        if num == 0:
            break
        sequence_sum += num

    print(sequence_sum)


if __name__ == '__main__':
    main()
