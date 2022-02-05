def main():
    sequence_sum = 0
    num = int(input())
    while num != 0:
        sequence_sum += num
        num = int(input())
    print(sequence_sum)


if __name__ == '__main__':
    main()
