from typing import List


class Solution:
    def containsDuplicate_dict(self, nums: List[int]) -> bool:
        flag = False
        hashmap = {}

        for el in nums:
            if el not in hashmap:
                hashmap[el] = 0
            else:
                return True

        return flag

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        hashset = set()

        for el in nums:
            if el not in hashset:
                hashset.add(el)
            else:
                return True

        return False


def main():
    solution = Solution()
    nums = list(map(int, input().split()))
    res = solution.containsDuplicate_set(nums)
    print(res)

    assert solution.containsDuplicate_set([1, 2, 3, 1]) is True
    assert solution.containsDuplicate_set([1, 2, 3, 4]) is False
    assert solution.containsDuplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


if __name__ == '__main__':
    main()
