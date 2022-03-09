def main():
    x, y, z = list(map(float, input().split()))
    n = int(input())
    eps = 10e-6
    real_x, real_y, real_z = 0, 0, 0

    for _ in range(n):
        a_i, b_i, c_i, q_i = list(map(float, input().split()))
        real_x += a_i * q_i
        real_y += b_i * q_i
        real_z += c_i * q_i

    if real_x >= x - eps and real_y >= y - eps and real_z >= z - eps:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
