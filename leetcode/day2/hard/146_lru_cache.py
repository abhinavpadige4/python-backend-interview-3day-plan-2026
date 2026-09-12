"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {3=3, 4=4}
lRUCache.get(1);    // returns -1 (not found)
lRUCache.get(3);    // returns 3
lRUCache.get(4);    // returns 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.
        
        Time Complexity: O(1)
        Space Complexity: O(capacity)
        
        Args:
            capacity: Positive integer representing the cache capacity
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        Also moves the accessed key to the end (most recently used).
        
        Time Complexity: O(1) - OrderedDict operations are O(1) average
        Space Complexity: O(1)
        
        Args:
            key: Integer key to retrieve
            
        Returns:
            Value associated with the key, or -1 if not found
        """
        if key not in self.cache:
            return -1
        
        # Move the accessed item to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. 
        Otherwise, add the key-value pair to the cache. 
        If the number of keys exceeds the capacity, evict the least recently used key.
        
        Time Complexity: O(1) - OrderedDict operations are O(1) average
        Space Complexity: O(1) amortized
        
        Args:
            key: Integer key to insert or update
            value: Integer value to associate with the key
        """
        if key in self.cache:
            # Update existing key and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # If we exceed capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove first item (least recently used)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from the problem
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)   # cache is {1=1}
    lRUCache.put(2, 2)   # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1    # return 1
    lRUCache.put(3, 3)   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1   # returns -1 (not found)
    lRUCache.put(4, 4)   # LRU key was 1, evicts key 1, cache is {3=3, 4=4}
    assert lRUCache.get(1) == -1   # returns -1 (not found)
    assert lRUCache.get(3) == 3    # returns 3
    assert lRUCache.get(4) == 4    # returns 4
    
    # Test case 2: Capacity 1
    lRUCache2 = LRUCache(1)
    lRUCache2.put(1, 1)
    assert lRUCache2.get(1) == 1
    lRUCache2.put(2, 2)  # Evicts key 1
    assert lRUCache2.get(1) == -1
    assert lRUCache2.get(2) == 2
    
    # Test case 3: Updating existing key
    lRUCache3 = LRUCache(2)
    lRUCache3.put(1, 1)
    lRUCache3.put(2, 2)
    lRUCache3.put(1, 10)  # Update existing key
    assert lRUCache3.get(1) == 10
    assert lRUCache3.get(2) == 2
    lRUCache3.put(3, 3)   # Evicts key 2
    assert lRUCache3.get(2) == -1
    assert lRUCache3.get(1) == 10
    assert lRUCache3.get(3) == 3
    
    # Test case 4: Sequential access
    lRUCache4 = LRUCache(3)
    for i in range(1, 4):
        lRUCache4.put(i, i)  # Cache: {1=1, 2=2, 3=3}
    
    assert lRUCache4.get(1) == 1  # Access 1, cache: {2=2, 3=3, 1=1}
    lRUCache4.put(4, 4)           # Evicts 2, cache: {3=3, 1=1, 4=4}
    assert lRUCache4.get(2) == -1
    assert lRUCache4.get(3) == 3
    assert lRUCache4.get(4) == 4
    
    print("All tests passed!")