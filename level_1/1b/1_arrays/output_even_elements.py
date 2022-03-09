def main():
    n = int(input())
    array = list(map(int, input().split()))
    sliced_array = [str(el) for el in array if el % 2 == 0]
    result_string = " ".join(sliced_array)

    print(result_string)


if __name__ == '__main__':
    main()
