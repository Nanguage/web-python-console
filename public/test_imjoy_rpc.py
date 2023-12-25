import numpy as np

import micropip
await micropip.install("imjoy-rpc")
import imjoy_rpc.rpc


rpc = imjoy_rpc.rpc.RPC(None, None)
arr = np.random.rand(10)
obj = rpc._encode(arr)
print(obj)
