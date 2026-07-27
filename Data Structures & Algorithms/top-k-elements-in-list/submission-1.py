class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        freqs = []
        for num, freq in hashmap.items():
            freqs.append([freq, num])
        freqs.sort()

        result = []
        while(len(result) < k):
            result.append(freqs.pop()[1])
        return result

