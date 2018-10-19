import LRU_p as lru

obj = lru.LRUCache(5)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
obj.put(5,5)
obj.put(6,6)
obj.get(2)
obj.printLRU()
obj.put(7,7)
print(obj._cache.keys())
