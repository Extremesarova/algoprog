class Solution:
    def isPalindrome_1(self, x: int) -> bool:
        '''
        Original solution using strings
        :param x:
        :return:
        '''
        if x < 0 or x != int(str(x)[::-1]):
            return False
        else:
            return True

    def isPalindrome_2(self, x: int) -> bool:
        '''
        Original solution using strings
        :param x:
        :return:
        '''
        return str(x) == str(x)[::-1]

    def isPalindrome_3(self, x: int) -> bool:
        '''
        Original solution using strings
        :param x:
        :return:
        '''
        original_number = x
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        while x != 0:
            remainder = x % 10
            reversed_number = reversed_number * 10 + remainder
            x //= 10
        return reversed_number == original_number


def main():
    solution = Solution()
    x = 123321
    res = solution.isPalindrome_3(x)
    print(res)


if __name__ == '__main__':
    main()





