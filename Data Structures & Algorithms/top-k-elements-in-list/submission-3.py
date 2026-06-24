class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contains={}
        result=[]
        for ch in nums:
            if ch not in contains:
                contains[ch]=1
            else:
                contains[ch]+=1
        pair = sorted(contains.items(), key=lambda x: x[1], reverse=True)
        for num,freq in pair[:k]:
            result.append(num)
        return result

