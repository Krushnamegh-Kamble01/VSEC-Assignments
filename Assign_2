import numpy as np

# ---------- NumPy basics ----------
arr = np.array([10, 20, 30, 40])
print(arr)
# [10 20 30 40]

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
# (4,)

print(arr[3])
# 40

print(arr[::-1])
# [40 30 20 10]

print(np.mean(arr))
# 25.0

print(np.sum(arr))
# 100

print(np.max(arr))
# 40

print(matrix.dtype)
# int32   (int64 on Linux/Mac; int32 was on Windows)

print(matrix.shape)
# (2, 3)

# ---------- Lists ----------
list = [1, "cat", 3, "tree"]
print(list)
# [1, 'cat', 3, 'tree']

print(type(list))
# <class 'list'>

print(dir(list))
# [..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ---------- Tuples ----------
tupple = (1, "cat", 3, "tree")
print(dir(tupple))
# [..., 'count', 'index']

# ---------- List methods ----------
list = [1, "cat", 3, "tree"]
list.append(3)
print(list)
# [1, 'cat', 3, 'tree', 3]

print(list.count("tree"))
# 1

list.clear()
print(list)
# []

list = [1, "cat", 3, "tree"]
list1 = list.copy()
print(list1)
# [1, 'cat', 3, 'tree']

print(list.index("tree"))
# 3

list.insert(0, 2)
print(list)
# [2, 2, 1, 'cat', 3, 'tree']   <- this cell was run twice in the notebook;
#                                  a single run gives [2, 1, 'cat', 3, 'tree']

list.pop()
print(list)
# [2, 2, 1, 'cat', 3]

list.remove(1)
print(list)
# [2, 2, 'cat', 3]

list.reverse()
print(list)
# [3, 'cat', 2, 2]

list2 = [1, 4, 5, 7, 2]
list2.sort()
print(list2)
# [1, 2, 4, 5, 7]

list.extend("cat")
print(list)
# [3, 'cat', 2, 2, 'c', 'a', 't', 'c', 'a', 't']

# ---------- Tuple methods ----------
tupple = (1, "cat", 3, "tree")
print(tupple.count(1))
# 1

print(tupple.index(3))
# 2

# ---------- Sets ----------
set1 = {1, "cat", 3, "tree"}
print(dir(set1))
# [..., 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#  'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
#  'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
#  'union', 'update']

set2 = {1, 2, 3, 4, 6, 7, 8, 9}
print(set1.union(set2))
# {1, 2, 3, 4, 6, 7, 8, 9, 'cat', 'tree'}

print(set1.difference(set2))
# {'cat', 'tree'}

# This one raised an error in the notebook (the method is called issubset, not subset):
# set1.subset(set2)
# AttributeError: 'set' object has no attribute 'subset'
print(set1.issubset(set2))
# False
