class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = collections.Counter(nums)

        return [item[0] for item in countdict.most_common(k)]