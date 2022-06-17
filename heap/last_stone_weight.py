import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # invert every element in list
        stones = [-1 * stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                if stones:
                    continue
                else:
                    return 0

            # smaller because min heap
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)

        return -stones[0]