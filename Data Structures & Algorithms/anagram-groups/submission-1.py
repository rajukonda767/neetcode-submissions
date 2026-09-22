class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            pattern=[0]*26
            for ch in s:
                pattern[ord(ch)-97]+=1
            
            res[tuple(pattern)].append(s)
        return list(res.values())