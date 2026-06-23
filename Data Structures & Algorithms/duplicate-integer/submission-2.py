class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cleaned=set(nums)
        if len(nums)==len(cleaned):
            return False
        else:
            return True