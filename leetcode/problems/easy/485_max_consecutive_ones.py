from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local_max = 0
        global_max = 0

        for el in nums:
            if el == 1:
                local_max += 1
            else:
                local_max = 0

            if local_max > global_max:
                global_max = local_max

        return global_max


def main():
    solution = Solution()
    nums = list(map(int, input().split()))
    res = solution.findMaxConsecutiveOnes(nums=nums)
    print(res)

    assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2


if __name__ == '__main__':
    main()
