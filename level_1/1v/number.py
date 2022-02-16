def get_comma(counter, i):
    return [","] if counter == 2 and i != 0 else [""]


def update_counter(counter):
    return 0 if counter == 2 else counter + 1


def add_commas(num):
    counter = 0
    lengths_num = len(num)
    num_with_commas = []

    for i in range(lengths_num - 1, -1, -1):
        digit = num[i]
        num_with_commas = get_comma(counter, i) + [digit] + num_with_commas
        counter = update_counter(counter)

    return "".join(num_with_commas)


def main():
    num = input()
    num_with_commas = add_commas(num)
    print(num_with_commas)

    # assert add_commas("12345678") == "12,345,678"
    # assert add_commas("999") == "999"
    # assert add_commas("1000") == "1,000"


if __name__ == '__main__':
    main()
