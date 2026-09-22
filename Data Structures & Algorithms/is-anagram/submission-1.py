class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq_s=defaultdict(int)

        for ch in s:
            freq_s[ch]+=1
        
        for ch in t:
            if ch in freq_s and freq_s[ch]>0:
                freq_s[ch]-=1
            else:
                return False
        
        return True
        
