import numpy as np

arr = np.random.rand(10)
print(arr)
obj = imjoy_encode(arr)
print()
print(obj)
decoded = imjoy_decode(obj)
print()
print(decoded)
