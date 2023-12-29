import numpy as np

arr = np.random.randint(0, 255, (200, 200), dtype=np.uint8)

ij = await api.createWindow(src="https://ij.imjoy.io")
await ij.viewImage(arr)
