class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse="".join(ch for ch in s if ch.isalnum()).lower()
        return reverse==reverse[::-1]