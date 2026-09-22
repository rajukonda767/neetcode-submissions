class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)

        for num in nums:
            freq[num]+=1
        
        return list(sorted(freq,key=lambda x:-freq[x]))[:k]