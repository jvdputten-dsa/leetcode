class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1

        for ix, digit in enumerate(digits):
            digits[ix] += carry
            if digits[ix] == 10:
                digits[ix] = 0
                if ix == len(digits) - 1:
                    digits.append(0)
            else:
                break

        return digits[::-1]