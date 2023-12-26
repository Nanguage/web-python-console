import imjoy_rpc.rpc

def imjoy_encode(arr):
    rpc = imjoy_rpc.rpc.RPC(None, None)
    obj = rpc._encode(arr)
    return obj
