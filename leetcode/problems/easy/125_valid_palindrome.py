class Solution:
    def isalnum(self, c: str) -> bool:
        return ("a" <= c.lower() <= "z") or ("0" <= c <= "9")

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:

            while l < r and not self.isalnum(s[l]):
                l += 1
                continue

            while r > l and not self.isalnum((s[r])):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


def main():
    solution = Solution()
    s = input()
    res = solution.isPalindrome(s)
    print(res)

    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True


if __name__ == '__main__':
    main()
