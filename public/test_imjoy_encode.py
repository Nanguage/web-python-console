import numpy as np
import imjoy_rpc.rpc


rpc = imjoy_rpc.rpc.RPC(None, None)
arr = np.random.rand(10)
obj = rpc._encode(arr)
print(obj)
