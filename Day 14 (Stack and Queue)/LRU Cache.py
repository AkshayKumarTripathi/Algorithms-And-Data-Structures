# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
# add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.


# Follow up:
# Could you do get and put in O(1) time complexity?


# We are going to use a doubly linked list (for constant time deletion) and a hashmap (dict) for constant time lookup.

class Node:
    def __init__(self,key:int, value:int):
        self.value=value
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self,capacity:int):
        self.size=0
        self.max=capacity
        self.head=Node('Head',None)
        self.tail=Node('tail',None)
        self.head.next=self.tail
        self.lookup={}

    def get(self,key:int) ->int :
        if key in self.lookup.keys():
            temp=self.lookup[key]
            self._remove(temp)
            del self.lookup[key]
            self.put(key,temp.value)
            return temp.value

        else:   return -1

    def put(self,key:int,value:int) ->None :
        if key in self.lookup.keys():
            temp=self.lookup[key]
            self._remove(temp)
            del self.lookup[key]
            self.put(key,value)
    
        elif self.size<self.max:
            temp=Node(key,value)
            self.lookup[key]=temp
            head_next=self.head.next
            self.head.next=temp
            temp.prev=self.head
            temp.next=head_next
            head_next.prev=temp
            self.size+=1

        else:
            temp=self.tail.prev
            self._remove(temp)
            del self.lookup[temp.key]
            self.put(key,value)

    def _remove(self,key):
        self.size-=1
        prev_key=key.prev
        next_key=key.next
        prev_key.next=next_key
        next_key.prev=prev_key
        del key


lRUCache=LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)

print(lRUCache.get(1))
print(lRUCache.get(2))


# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))