from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        min_length = len(min(strs))
        for i in range(min_length + 1):
            x = [str[:i] for str in strs]
            if len(strs) == x.count(x[0]):
                prefix = x[0]
            else:
                break
        return prefix

    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        min_length = len(min(strs))
        for i in range(min_length + 1):
            x = [str[:i] for str in strs]
            if len(strs) == x.count(x[0]):
                prefix = x[0]
            else:
                break
        return prefix


def main():
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
