def main():
    n = int(input())
    heights = map(int, input().split())
    target_hight = int(input())

    place = -1

    for i, height in enumerate(heights):
        if target_hight > height:
            place = i + 1
            break
    if place == -1:
        place = n + 1

    print(place)


if __name__ == '__main__':
    main()
