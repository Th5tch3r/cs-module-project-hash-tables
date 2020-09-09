## Review proj
## Code our hash functions
## Collision: how to handle
## Load Factor
## Stretch goals: hash function applications


## In general, crypto is hard
### It takes any string as input
### Deterministic
### Non-reversible

### May have to generate a "secret" that the function uses to hash


# COLLISIONS
## How should we handle?
## Disallow ut?
## Open addressing: linear probing, quadratic probing

## Linked list aka chaining
## We're gonna make an array of linked lists
## data structure compositions

buckets = [None] * 8

buckets = [
    None,
    Node('foo', 'bar') --> Node('foooz', 'fub') --> Node('zug', 'ixq')
    None,
    Node('quux', 'baz'),
    None,
    None,
    None,
    None,
]

put('foo', 'bar') # index 1
put('quux', 'baz') # index 3
put('foooz', 'fub') # "foooz" hashes to index 1
put('zug', 'ixq') # "zug" hashes to index 1

get('foooz') # go to index 1, iterate through and find the same key, return value 'fub'

put('zug', 'ziggy') # go to index 1, iterate through and find the same key, overwrite

my_dict['a'] = 1
my_dict['a'] = 2

## time cost of iterating? O(n)?????
## How does the linked list and array work together in memory?

## storing ket is a bad idea if you're hashing passwords
## but for hash table it's okay

## Put
### hash your key, mod by len of your array to get your index
### If index is None, put your Node there
### If not None, iterate through 
#### If the same key is found, overwrite
#### If not, append to the head or tail

## Get
### hash your key, mod by len of your array to get your index
### If index is None, return None
### If index is not None, iterate through and find matching key and return the value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def find(self, val):
        # assign a cur_node
        cur_node = self.head
        # while cur_node is not None
        while cur_node is not None:
            # check the value
            # if self.value = val
            if val = cur_node.value:
                # return self.val
                return cur_node.value
            # self cur_node = cur_node.next
            else:
                cur_node = cur_node.next
        
        return None
    
    def add_to_tail(self, val):
        """
        Check if we have a head
        If so, find the tail and add a node
        """
        # Start with head
        # if head is None, make a node and add it
        if self.head is None:
            self.head = Node(val)
        else: 
        # otherwist, iterate through and find the tail
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next

ll = LinkedList()
nl = Node(3)

ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)