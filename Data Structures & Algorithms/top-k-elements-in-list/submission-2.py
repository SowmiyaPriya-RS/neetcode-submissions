class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        freqs = [[] for i in range(len(nums)+1)]
        for num, freq in hashmap.items():
            freqs[freq].append(num)

        result = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if(len(result) == k):
                    return result

