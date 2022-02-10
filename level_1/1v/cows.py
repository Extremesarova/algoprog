def main():
    n = int(input())
    base_string = f'{n} korov'
    final_string = base_string

    if n < 11 or n > 20:
        if 2 <= n % 10 <= 4:
            final_string = base_string + 'y'
        elif n % 10 == 1:
            final_string = base_string + 'a'

    print(final_string)


if __name__ == '__main__':
    main()
