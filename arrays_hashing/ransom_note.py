class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        for char in magazine:
            if char in ransomNote:
                try:
                    index = ransom_list.index(char)
                except ValueError:
                    continue
                ransom_list.pop(index)

                if not ransom_list:
                    return True

        return False