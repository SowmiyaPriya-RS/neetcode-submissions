class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if(len(t) > len(s)):
            return ""
            
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        have = 0
        need = len(countT)
        window = {}
        res = [-1, -1]
        reslen = float("infinity")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while(have == need):
                if((r-l+1) < reslen):
                    res = [l, r]
                    reslen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""



        