class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.squares(n)
            if(n == 1):
                return True
        return False

    def squares(self, n:int) -> int:
        total = 0
        while n:
            digit = n%10
            digit = digit**2
            total += digit
            n = n//10
        return total

        