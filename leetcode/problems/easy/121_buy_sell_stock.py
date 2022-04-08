from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r

            r += 1

        return max_profit


def main():
    solution = Solution()
    prices = list(map(int, input().split()))
    res = solution.maxProfit(prices)
    print(res)

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == '__main__':
    main()
