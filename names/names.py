from binary_search_tree import BinarySearchTree

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)    ### runtime = ~4 sec

# My replacement 
binaryST = BinarySearchTree('Hallie Vazquez')

for n1 in names_1:
    binaryST.insert(n1)

for n2 in names_2:
    if binaryST.contains(n2):
        duplicates.append(n2)

### runtime = ~0.094 seconds 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


st = time.time()
duplicates = list(set(names_1).intersection(set(names_2)))
et = time.time()

print(f"Duplicates: {len(duplicates)} \n\n{', '.join(duplicates)}\n\n")
print(f"Runtime: {et - st} seconds") ### Runtime = ~0.001 seconds 