import numpy as np

print(np.random.randn(3, 3))
# [[-0.89683369 -0.67388396 -0.32950366]
#  [-0.26021397 -1.8265589   1.00643877]
#  [-2.0938757  -0.15549686 -0.2819091 ]]

print(np.random.rand(1, 2))
# [[0.41534444 0.66212043]]

print(np.random.randint(0, 100, 5))
# [48 25 67 53 18]

np.random.seed(42)
uniform = np.random.randn(5)
normal = np.random.randn(1000)
ints = np.random.randint(1, 7, 10)
print("mean:", np.mean(normal))
print("standard deviation:", np.std(normal))
print("variance:", np.var(normal))
print("median:", np.median(normal))
# mean: 0.019471946976027023
# standard deviation: 0.9790620578368584
# variance: 0.9585625130957439
# median: 0.026488444602682282

a = np.array([1, 2, 3, 4, 5])
print(np.random.choice(a, 10))
# [2 2 3 1 4 2 3 2 4 4]

print(np.mean(a))
# 3.0

print(np.var(a))
# 2.0

print(np.median(a))
# 3.0

print(np.percentile(a, 100))
# 5.0
