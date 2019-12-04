# get(key)
# put(key, value)

# size 3 put 1 put 2 put 3 put 4 - evict 1

class Node(object):
    def __init__(self, prev_node, next_node, value, key):
        self.prev_node = prev_node
        self.next_node = next_node
        self.value = value
        self.key = key
        
    def __repr__(self):
        return 'prev value: {} value: {} next_value{}'.format(self.prev_node.value if self.prev_node else None, self.value, self.next_node.value if self.next_node else None,)

class LRU:
    def __init__(self, size):
        self.size = size
        self.map = {}
        self.last = None
        self.first = None
        
    def __repr__(self):
        return 'first: {} last: {}'.format(self.first, self.last)
    
    def get(self, key):
        node = self.map.get(key)
        
        if node:
            value = node.value
            prev_node = node.prev_node
            next_node = node.next_node
            
            if prev_node:
                prev_node.next_node = next_node
            else:
                self.first = next_node
            
            if next_node:
                next_node.prev_node = prev_node
            
            last = self.last
            last.next_node = node
            node.prev_node = last
            node.next_node = None
            self.last = node
            
            return value

        return None
    
    def put(self, key, value):
        if self.get(key):
            node = self.map[key]
            node.value = value
            
        else:
            last = self.last
            if last:
                node = Node(last, None, value, key)
                last.next_node = node
                
            else:
                node = Node(None, None, value, key)
                self.first = node
                
            self.last = node
            self.map[key] = node
            
            if len(self.map) > self.size:
                first = self.first
                new_first = first.next_node
                new_first.prev_node = node
                
                self.first = new_first
                self.map.pop(first.key)

            
            
lru = LRU(3)

lru.put('a', 1)
lru.put('b', 2)
lru.put('c', 3)

print lru

lru.put('d', 4)

print lru

print lru.get('a')
print lru

print lru.get('b')
print lru