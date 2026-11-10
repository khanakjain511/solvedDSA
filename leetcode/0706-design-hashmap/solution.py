# Runtime: 70 ms
# Memory: 22.5 MB

class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
                
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
                
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)