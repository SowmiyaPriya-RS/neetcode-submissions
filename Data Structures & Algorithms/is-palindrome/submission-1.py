class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i != ' ' and i.isalnum():
                string += i.lower()
        rev = string[::-1]
        print(string)
        print(rev)
        for i in range(len(string)):
            if(string[i] != rev[i]):
                return False
        return True