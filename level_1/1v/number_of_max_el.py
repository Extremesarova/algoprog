def main():
    d = {}
    max_val = - 1
    val = int(input())
    while val != 0:
        d[val] = d[val] + 1 if val in d else 1
        if val > max_val:
            max_val = val
        val = int(input())

    print(d[max_val])


if __name__ == '__main__':
    main()
