class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i,ch in enumerate(nums):
            container=target-ch
            if container in result:
                return [result[container],i]
            else:
                result[ch]=i
