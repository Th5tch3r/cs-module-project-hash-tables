

my_arr = ["hi", "world", "how", "are", "you", "lorem", "ipsum", "set"]

# Search for an element in this arr

##O(n) -- linear search
def find_element(arr, el):
    for thing in arr:
        if thing == el:
            return True

    return False

## Or if we sorted, binary search!
## O(log n)

## Which Big O complexities are faster than log n?
## Constant time! 0(1)
### If we increase the input, we still take number of steps to find what we're looking for

# def magic_fun_find_index(arr, el):
#     return el_index 

# idx = magic_fun_find_index(my_arr, "set") ## 7
# my_arr[idx] # ta-da

## has tables == arrays + hashing function

## Write a function that will take a string and return a number
def len_hash(str):
    return len(str)
## A lof of collisions
print(len("sad") == len("was"))
len("ball") == len("hats")

# Fast
# Determinist

## We could map letters to numbers, but that's already been done!
# ASCII was the first mapping of letters to numbers
## UTF-8 is ASCII on steroids, designed to work with ASCII but be univeral
### 
# use .endcode()

## a: 1
## b: 2

def UTF8_hash(str):
    # for letter in str:
    #     val = ord(letter)
    #     total += val
    total = 0
    utf_bytes = str.encode()
    for byte in utf_bytes:
        total += byte

    return total

print(UTF8_hash("sad"))
print(UTF8_hash("Was"))

# but we will still have collisions
### to be continued!
UTF8_hash("dad")
UTF8_hash("add")

print(UTF8_hash("supercalifragilisticexpialidocious")) ## 3643

# A hash function: takes string, gives back number
## operate on the bytes that make up the string
## Deterministic 

## To improve our hash function, make output more unique!
## SHA256

## Hash function + array!
## Hash function gives us back some big number
### How to map the output of our has function to an index in an array?

# my_arr2 = [None] * 20

# idx = UTF8_hash("supercalifragilisticexpialidocious") ## 3643

# my_arr2[idx] = "Mary Poppins"

## how to turn result of hash function into usable index?
### modulo the hash with len(my_arr2)

## Modulo demonstration
## Modulo returns from 0 to len(list) - 1
# 1 % 20 --> 1
# 15 % 20 --> 15
# 20 % 20 --> 0
# 21 % 20 --> 1
# 22 % 20 --> 2
# 39 % 20 --> 19
# 40 % 20 --> 0

# Use modulo with hash (output of hashing function) to get usable index

## we can now combine  hash and array
## "put" into our array
my_arr2 = [None] * 20000

our_hash = UTF8_hash("supercalifragilisticexpialidocious") ## 3643
idx = our_hash % len(my_arr2) 

my_arr2[idx] = "Mary Poppins"

# print(my_arr2)

# "get"
our_hash = UTF8_hash("supercalifragilisticexpialidocious")
idx = our_hash % len(my_arr2)

# print(my_arr2[3])
val = my_arr2[idx]
print(val)

# Key value pair
# "supercalifragilisticexpialidocious" if the key
# "Mary Poppins" is the value

# Hash table in programming languages?
## Python: dictionary
## JS: object
## Hash map
## Map


## Pseudocode for put
### 1. Hash the key
### 2. Take the hash and mod it with len of array
### 3. Go to index and put in value

## Pseudocode for get
### 1. Hash the key
### 2. Take the hash and mod it with len of array
### 3. Go to index and get out the value

## Time complexity?
### Same for get and put
#### Linear in length of string/key
#### Constant time in length of array <----- This is what we pay attention to
# O(1)

## Collision
key1 = "dad"
key2 = "add"

### Put 1
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = "howdy"

print(my_arr2[idx1])

### Put 2
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = "whats up yall"

### Get
get_hash = UTF8_hash(key1)
idx3 = get_hash % len(my_arr2)
print(my_arr2[idx3])

## Even when we use out hash function with modulo, we get collisions
### To be solved later

## We wrote our own hash function, what about Python's hash()?
### Many different hash functions! Can also hash()

### When used with hash tables, hasing function should be FAST 
#### Why? we want O(1), and a lot of lookups

## Other uses of hash functions
### passwords!! e.g., bcryptjs
### Encryption/decryption

## password --> hashing function --> hashed_password
## password --> hashing function --> hash === hashed_password??

### Here hash function should be slow
#### 1234mypassword


### SHA-256 has never had a collision
#### can use the output (hash) as a fingerprint for your string
my_string = "Dear everybody, how are you? I write to you..."
