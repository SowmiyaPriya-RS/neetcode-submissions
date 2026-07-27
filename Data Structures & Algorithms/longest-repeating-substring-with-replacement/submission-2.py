class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_freq = 0
        hashmap = {}
        l = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            max_freq = max(max_freq, hashmap[s[r]])
            if((r-l+1)-max_freq > k):
                hashmap[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
        return result


        