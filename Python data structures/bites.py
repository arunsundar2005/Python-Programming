v = b'arun' # Initialization of a byte

print(v) # Output: b'arun'

print(v.split())
"""Output
[b'arun']
"""
print(v.split(b'r')) # Output -> [b'a', b'un']

print(v.swapcase()) # Output -> b'ARUN'

