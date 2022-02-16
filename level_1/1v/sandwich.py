def decode_string(s):
    lengths_s = len(s)
    original_s = ['0'] * lengths_s

    counter_start = 0
    counter_end = 1

    for i in range(lengths_s):
        if i % 2 == 0:
            original_s[counter_start] = s[i]
            counter_start += 1
        else:
            original_s[lengths_s - counter_end] = s[i]
            counter_end += 1
    return "".join(original_s)


def main():
    s = input()[:-1]
    original = decode_string(s)
    print(original)

    # assert decode_string("Aabrrbaacda") == "Abracadabra"


if __name__ == '__main__':
    main()
