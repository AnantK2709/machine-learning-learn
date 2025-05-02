# Automatic garbage collection, reference counting, and memory leaks

# Reference Counting
import sys
a=[]
print(sys.getrefcount(a)) # 2 one for the variable a and one for the argument in getrefcount

b = a
print(sys.getrefcount(a)) # 3 one for the variable a, one for the argument in getrefcount and one for b

del b
print(sys.getrefcount(a)) # 2 one for the variable a and one for the argument in getrefcount


### Garbage Collection
# The garbage collector is a built-in module in Python that provides an interface to the garbage collection facility.
import gc
# enable garbage collection
gc.enable()
# print(gc.collect())
# print(gc.get_stats())
# print(gc.get_count())



# Efficient Memory Management
# 1, Use local variables instead of global variables
# 2, Use built-in data types and libraries
# 3, Use generators instead of lists
# 4, Use the with statement to manage resources
# 5. Avoid cicular references

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")
    def __del__(self):
        print(f"Object {self.name} deleted")

# Create a circular reference
a = MyObject("a")
b = MyObject("b")
a.ref = b
b.ref = a

del a # This will not delete the object immediately because of the circular reference, nothing would be deleted
del b

# Manual trigger the Garbage Collection
gc.collect()


# Generators for memory efficiency
def generate_numbers(n):
    for i in range(n):
        yield i

# using the generator
for number in generate_numbers(1000000):
    print(number)
    if number > 10:
        break


# Profiling memory usage
import tracemalloc

def create_large_list():
    return [i for i in range(1000000)]
def main():
    tracemalloc.start()
    create_large_list()
    snapshot1 = tracemalloc.take_snapshot()
    large_list = create_large_list()
    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)
    tracemalloc.stop()
if __name__ == "__main__":
    main()