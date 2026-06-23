class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contain={}
        for word in strs:
            keys=''.join(sorted(word))
            if keys not in contain:
                contain[keys]=[]
            contain[keys].append(word)
        return list(contain.values())
