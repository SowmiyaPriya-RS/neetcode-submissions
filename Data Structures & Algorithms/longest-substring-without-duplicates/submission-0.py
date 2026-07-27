class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]]+1)
            hashmap[s[r]] = r
            length = max(length, r-l+1)
        return length


        