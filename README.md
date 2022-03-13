# MRUCache
Implementing a data structure for Most Recently Used (MRU) cache using Python. 
It should support the following operations: get and put.
* get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
* put(key, value) – Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the Most recently used item before inserting a new item.
The cache is always initialized with positive capacity.

My solution is to use the power of OrderedDict from collections module which keep order of insertion of keys and we can change that order if required. The best part is all operations have O(1) time complexity.

Input/Output:
Mycache=MRUCache(3)
Mycache.put(1,1)
Mycache.put(2,2)
Mycache.put(3,3)
print(Mycache.cache)  // OrderedDict([(1, 1), (2, 2), (3, 3)])
Mycache.get(1)        // returns 1
print(Mycache.cache)  // OrderedDict([(2, 2), (3, 3), (1, 1)])
Mycache.get(4)        // returns -1 (Not found)
Mycache.put(4,4)      // evicts key 1 
print(Mycache.cache)  // OrderedDict([(2, 2), (3, 3), (4, 4)])
Mycache.put(3,5)      // Update existing key 
print(Mycache.cache)  // OrderedDict([(2, 2), (4, 4), (3, 5)])
