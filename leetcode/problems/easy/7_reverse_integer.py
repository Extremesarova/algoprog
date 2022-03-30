INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1


class Solution:
    def reverse_1(self, x: int) -> int:
        '''
        Reversing a string
        :param x:
        :return:
        '''
        reverse = ''
        str_x = str(x)
        if str_x[0] == '-':
            reverse += str_x[0]
            str_x = str_x[1:]
        reverse += str_x[::-1]
        reverse = int(reverse)
        if INT_MIN <= reverse <= INT_MAX - 1:
            return int(reverse)
        else:
            return 0

    def reverse_2(self, x: int) -> int:
        '''
        Proper solution
        :param x:
        :return:
        '''
        abs_x = abs(x)
        rev = 0
        while abs_x != 0:
            pop = abs_x % 10
            abs_x //= 10
            if rev > INT_MAX / 10 or (rev == INT_MAX / 10 and pop > 7):
                return 0
            if rev < INT_MIN / 10 or (rev == INT_MIN / 10 and pop < -8):
                return 0
            rev = rev * 10 + pop
        if x < 0:
            rev = - rev
        return rev


def main():
    solution = Solution()
    x = -123
    res = solution.reverse_2(x)
    print(res)


if __name__ == '__main__':
    main()
