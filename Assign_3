import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

add = a + b
print("addition:", add)
sub = a - b
print("substraction:", sub)
print("multiplication:", a * b)
print("division:", a / b)
# addition: [11 22 33 44 55]
# substraction: [ -9 -18 -27 -36 -45]
# multiplication: [ 10  40  90 160 250]
# division: [0.1 0.1 0.1 0.1 0.1]

print(np.exp(a))
# [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]

c = np.array([4, 9, 25, 36, 49])
print(np.sqrt(c))
# [2. 3. 5. 6. 7.]

print(np.subtract(b, a))
# [ 9 18 27 36 45]

print(np.power(a, 2))
# [ 1  4  9 16 25]

print(np.sin(a) / np.cos(b))
# [-1.00285966  2.228222    0.9148699   1.1347418  -0.99373889]

print(np.log(a))
# [0.         0.69314718 1.09861229 1.38629436 1.60943791]

print(np.abs(a))
# [1 2 3 4 5]

# ---------- Broadcasting ----------
matrix = np.arange(12).reshape(3, 4)
row_vector = np.array([1, 0, 1, 0])
print(matrix + row_vector)
# [[ 1  1  3  3]
#  [ 5  5  7  7]
#  [ 9  9 11 11]]

col = np.array([[0], [10], [20]])
row = np.array([1, 2, 3])
print(col + row)
# [[ 1  2  3]
#  [11 12 13]
#  [21 22 23]]

# ---------- Statistics ----------
print(np.median(a))
# 3.0

print(np.min(a))
# 1

print(np.max(a))
# 5

print(np.percentile(a, 100))
# 5.0
