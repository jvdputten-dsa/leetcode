class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set(s)
        window_size = len(char_set)

        while True:
            for j in range(len(s) - window_size + 1):
                char_set = set(s[j:j + window_size])
                if len(char_set) == window_size:
                    return window_size

            window_size -= 1