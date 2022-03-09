def add_commas(num):
    counter = 0
    lengths_num = len(num)
    num_with_commas = ""

    for i in range(lengths_num - 1, -1, -1):
        comma = "," if counter == 2 and i != 0 else ""
        num_with_commas += num[i] + comma
        counter = 0 if counter == 2 else counter + 1

    return num_with_commas[::-1]


def main():
    num = input()
    num_with_commas = add_commas(num)
    print(num_with_commas)

    # assert add_commas("12345678") == "12,345,678"
    # assert add_commas("999") == "999"
    # assert add_commas("1000") == "1,000"


if __name__ == '__main__':
    main()
