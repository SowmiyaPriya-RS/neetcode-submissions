class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        lengths = []
        for s in strs:
            lengths.append(len(s))
        for l in lengths:
            result += str(l)
            result += ','
        result += '#'
        for s in strs:
            result += s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        lengths = []
        val = ""
        for i in range(len(s)):
            if(s[i] == '#'):
                pos = i
                break
            elif(s[i] == ','):
                lengths.append(int(val))
                val = ""
            else:
                val += s[i]
        s = s[pos+1:]
        for l in lengths:
            result.append(s[0:l])
            s = s[l:]
        return result

