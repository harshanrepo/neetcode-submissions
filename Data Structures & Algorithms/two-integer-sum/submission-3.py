class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,ch in enumerate(nums):
            container=target-ch
            if container in seen:
                return [seen[container],i]
            else:
                seen[ch]=i
        