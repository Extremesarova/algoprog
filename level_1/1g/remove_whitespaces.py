def get_cleaned_from_duplicated_whitespaces(s):
    cleaned_s = ""
    counter = 0
    for char in s:
        if char == " ":
            counter += 1
            if counter == 1:
                cleaned_s += char
            else:
                continue
        else:
            counter = 0
            cleaned_s += char
    return cleaned_s


def main():
    s = input()

    cleaned_s = get_cleaned_from_duplicated_whitespaces(s)
    print(cleaned_s)

    assert get_cleaned_from_duplicated_whitespaces(
        " nz d urp lren s bwz  boom  t a   j    ho    vi") == " nz d urp lren s bwz boom t a j ho vi"
    assert get_cleaned_from_duplicated_whitespaces("   d  iz  czl l l h udq t ") == " d iz czl l l h udq t "


if __name__ == '__main__':
    main()
