class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i,ch in enumerate(nums):
            container=target-ch
            if container in arr:
                return [arr[container],i]
            arr[ch]=i
        