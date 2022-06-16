class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for index, num in enumerate(nums):
            difference[target - num] = index

        for index, num in enumerate(nums):
            if num in difference:
                if index != difference[num]:
                    return [index, difference[num]]