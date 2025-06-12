my_set = {1,2,3}
# Unordered, mutable, no duplicates.

my_set.add(5)              # Add element
my_set.remove(3)           # Remove item
my_set.discard(6)          # Remove safely
my_set.clear()             # Remove all
my_set.update({6, 7})      # Add multiple

a = {1, 2, 3}
b = {3, 4, 5}
a.union(b)                 # {1, 2, 3, 4, 5}
a.intersection(b)          # {3}
a.difference(b)            # {1, 2}


for item in my_set:
    print(item)