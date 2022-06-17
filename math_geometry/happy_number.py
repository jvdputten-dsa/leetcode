class Solution:

    def digit_squares(self, n):
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        return total

    def isHappy(self, n: int) -> bool:

        record = set()

        while True:
            n = self.digit_squares(n)

            if n == 1:
                return True

            if n not in record:
                record.add(n)
            else:
                return False