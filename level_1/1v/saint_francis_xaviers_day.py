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

tasks = {
    0: ['Покормить кота'],
    1: ['Полить цветы', 'Забрать посылку', 'купить книгу', 'продать книгу', 'Полить цветы'],
    2: ['Почитать книгу по программированию', 'Почитать книгу по программированию', 'Открыть счет в банке'],
    3: ['Ответить на письмо двоюродной тети']
}

new_tasks = {priority: list(set(tasks_list)) for priority, tasks_list in tasks.items()}
