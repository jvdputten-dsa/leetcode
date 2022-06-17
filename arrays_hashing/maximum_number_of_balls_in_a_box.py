from collections import Counter

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count_map = Counter()

        for i in range(lowLimit, highLimit + 1):
            sum_of_digits = sum(int(digit) for digit in str(i))
            count_map[sum_of_digits] += 1

        return count_map.most_common(1)[0][1]