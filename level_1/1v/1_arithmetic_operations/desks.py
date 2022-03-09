def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    n_list = [n1, n2, n3]
    desks = sum([n // 2 + n % 2 for n in n_list])

    print(desks)


if __name__ == '__main__':
    main()
