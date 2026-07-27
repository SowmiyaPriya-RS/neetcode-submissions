class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha1 = [0]*26
        alpha2 = [0]*26

        for i in s:
            alpha1[ord(i)-ord('a')] += 1
        for i in t:
            alpha2[ord(i)-ord('a')] += 1

        for i in range(len(alpha1)):
            if(alpha1[i] != alpha2[i]):
                return False
        return True