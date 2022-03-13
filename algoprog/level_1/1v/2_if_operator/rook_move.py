def main():
    source_cell = (int(input()), int(input()))
    target_cell = (int(input()), int(input()))

    is_possible = 'YES'

    if source_cell[0] != target_cell[0] and source_cell[1] != target_cell[1]:
        is_possible = 'NO'

    print(is_possible)


if __name__ == '__main__':
    main()
