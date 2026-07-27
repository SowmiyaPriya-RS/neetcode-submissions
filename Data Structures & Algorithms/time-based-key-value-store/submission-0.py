class TimeMap:

    def __init__(self):
        self.key_value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_value:
            self.key_value[key] = []
        self.key_value[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.key_value.get(key, [])
        l = 0
        r = len(values)-1

        while(l<=r):
            mid = (l+r)//2
            if(values[mid][1] <= timestamp):
                result = values[mid][0]
                l = mid+1
            else:
                r = mid-1
        return result
            
        
