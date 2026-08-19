class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 1
        start = 0
        for i in range(n):
            l = i-1
            r = i+1
            while l>=0 and s[l] == s[i]:
                l -= 1
            while r<n and s[r] == s[i]:
                r += 1
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r-l-1
            if length > maxlen:
                maxlen = length
                start = l+1
        return s[start : start+maxlen]

        