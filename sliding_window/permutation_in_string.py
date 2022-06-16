class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        window_size = len(s1)
        s1 = sorted(s1)

        while l + window_size <= len(s2):
            substring = s2[l:l + window_size]
            if s1 == sorted(substring):
                return True
            else:
                l += 1

        return False