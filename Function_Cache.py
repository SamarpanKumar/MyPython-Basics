# import functools
from functools import lru_cache
import time

#@functools.lru_cache(maxsize=None)
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(20)) # Should print 100 after 5 seconds
print("done for 20")

print(fx(2))  # Should print 10 after 5 seconds
print("done for 2")

print(fx(6))  # Should print 30 after 5 seconds
print("done for 6")

# The following calls will be instant as they are cached
print(fx(20)) # Should print 100 instantly
print("done for 20")

print(fx(2))  # Should print 10 instantly
print("done for 2")

print(fx(6))  # Should print 30 instantly
print("done for 6")

print(fx(61)) # Should print 305 after 5 seconds (new computation)
print("done for 61")
