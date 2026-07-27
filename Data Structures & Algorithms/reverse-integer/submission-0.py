class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        res = 0

        while x:
            rem = int(math.fmod(x, 10))
            x = int(x / 10)
            res = (res*10) + rem
            print(res)
            if res > MAX or res < MIN:
                return 0   
        return res

        