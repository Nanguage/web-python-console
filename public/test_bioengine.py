import micropip
await micropip.install(['imjoy-rpc', 'kaibu-utils', 'pyodide-http', 'requests'])
# Patch requests
import pyodide_http
pyodide_http.patch_all()  # Patch all libraries

import matplotlib.pyplot as plt
#from pyotritonclient import execute
from imjoy_rpc.hypha import connect_to_server
from kaibu_utils import fetch_image

SERVER_URL = "https://ai.imjoy.io"

image = await fetch_image('https://zenodo.org/api/records/6647683/files/sample_input_0.tif/content')

server = await connect_to_server(
        {"server_url": SERVER_URL, "method_timeout": 3000}
    )
triton = await server.get_service("triton-client")

ret = await triton.execute(inputs=[{'inputs': None, "model_id": "powerful-chipmunk", 'return_rdf':True}],
                           model_name="bioengine-model-runner",
                           serialization="imjoy",
                          )
print(ret['result']['rdf'])

in_img = image[None, None, ...]

ret = await triton.execute(inputs=[{"inputs":[in_img], "model_id": "powerful-chipmunk"}],
                           model_name="bioengine-model-runner",
                           serialization="imjoy",
                          )
result = ret["result"]
mask = result['outputs'][0]
print('prediction: ', mask.shape)

# display the output
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(image)
ax1.set_title('input image')
ax2.imshow(mask[0][1])
ax2.set_title('predicted mask')
plt.show()