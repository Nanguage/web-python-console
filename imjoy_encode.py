import imjoy_rpc.rpc

def imjoy_encode(pyobj):
    rpc = imjoy_rpc.rpc.RPC(None, None)
    obj = rpc._encode(pyobj)
    return obj

def imjoy_decode(obj):
    import numpy as np
    rpc = imjoy_rpc.rpc.RPC(None, None)
    pyobj = rpc._decode(obj, False)
    return pyobj
