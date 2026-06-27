class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned=''.join(char for char in s if char.isalnum()).lower()
        reverse_cleaned=cleaned[::-1]
        return reverse_cleaned==cleaned