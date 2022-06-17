class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(cost) - 1):
            two, one = one, min(cost[i] + two, cost[i + 1] + one)

        return min(one, two + cost[-1])