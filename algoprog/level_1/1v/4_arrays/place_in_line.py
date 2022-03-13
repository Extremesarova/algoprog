def main():
    n = int(input())
    heights = map(int, input().split())
    target_hight = int(input())

    place = n + 1

    for i, height in enumerate(heights):
        if target_hight > height:
            place = i + 1
            break

    print(place)


if __name__ == '__main__':
    main()
