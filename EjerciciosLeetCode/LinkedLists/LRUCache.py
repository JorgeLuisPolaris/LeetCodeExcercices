"""
Design a data structure that follows the constraints of a Least Recently Used (LRU)
 cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
 the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val):
        self.key= key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to nodes
        self.left, self. right = Node(0,0), Node(0,0) #nodos más recientes y menos recientes, left es el LRU right el MRU
        self.left.next, self.right.prev = self.right , self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val #además de regresar se tiene que actualizar el más usado
        return -1

    #quita un nodo de cualquier lugar de la lista
    def removeNode(self,node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    #inserta hasta la derecha de la lista
    def insertNode(self,node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insertNode(self.cache[key])
        #si la longitud del cache se pasa de lo máximo se debe borrar el menos reciente
        if len(self.cache)> self.cap:
            lru = self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]


lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))  
print(lRUCache.put(2, 2)) 
print(lRUCache.get(1))
print(lRUCache.put(3, 3)) 
print(lRUCache.get(2))    
print(lRUCache.put(4, 4)) 
print(lRUCache.get(3))
print(lRUCache.get(4))    