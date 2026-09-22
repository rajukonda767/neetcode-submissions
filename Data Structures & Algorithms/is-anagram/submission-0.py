class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s=defaultdict(int)
        for ch in s:
            freq_s[ch]+=1
        
        for ch in t:
            if ch in freq_s:
                freq_s[ch]-=1
            else:
                return False
        
        for val in freq_s.values():
            if val!=0:
                return False
        return True
        
