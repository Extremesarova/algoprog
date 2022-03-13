def main():
    birth_year, death_year = map(float, input().split())
    beginning_date = 1605

    birth_diff = birth_year - beginning_date
    birth_diff = birth_diff if birth_diff >= 0 else -1
    # -1 indicates that the peasant was born before the church was built
    # to account for at least one time that he could touch the relics

    death_diff = death_year - beginning_date

    if death_diff < 0:
        counts = 0
    else:
        counts = int(death_diff // 10 - birth_diff // 10)

    print(counts)


if __name__ == '__main__':
    main()
