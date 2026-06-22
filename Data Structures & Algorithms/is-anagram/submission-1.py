class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = list(t)
        for letter in s:
            if letter in s_list:
                s_list.remove(letter)
            else:
                return False
        return True