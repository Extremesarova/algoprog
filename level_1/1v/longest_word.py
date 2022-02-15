def get_longest_word(words):
    lengths = [len(word) for word in words]
    max_len = max(lengths)
    max_index = lengths.index(max_len)
    max_word = words[max_index]

    return max_word, max_len


def main():
    words = input().split()

    max_word, max_len = get_longest_word(words)
    print(max_word)
    print(max_len)

    # assert get_longest_word("one two three four five six".split()) == ("three", 5)
    # assert get_longest_word("one two three four five six seven".split()) == ("three", 5)
    # assert get_longest_word(" one two three four five six seven ".split()) == ("three", 5)


if __name__ == '__main__':
    main()
