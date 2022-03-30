from typing import List


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force fixed a bit
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i, j]

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        """
        Two-pass Hash Table
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def twoSum_4(self, nums: List[int], target: int) -> List[int]:
        """
        One-pass Hash Table
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = solution.twoSum_3(nums=nums, target=target)
    print(res)

    assert set(solution.twoSum_3(nums=[2, 7, 11, 15], target=9)) == {0, 1}
    assert set(solution.twoSum_3(nums=[3, 2, 4], target=6)) == {1, 2}
    assert set(solution.twoSum_3(nums=[3, 3], target=6)) == {0, 1}


if __name__ == '__main__':
    main()
