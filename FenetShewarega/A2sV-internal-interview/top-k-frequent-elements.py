class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = []
        store = defaultdict(int)
        for i in nums:
            store[i] += 1
        
        sorted_store = sorted(store.items(), key=lambda x:x[1],reverse = True)
        for i in range(k):
            s.append(sorted_store[i][0])
        return(s)