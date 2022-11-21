from specklepy.api.client import SpeckleClient

# The code is roughly copied from speckles own documentation and examples, with a lot of trial and error

# https://speckle.guide/dev/py-examples.html
# https://speckle.guide/dev/py-sample.html
# https://github.com/specklesystems/speckle-docs/blob/9ed3f91f1f7f87f92d6e9cbaaa219f685c270350/user/web.md
# https://speckle.xyz/streams/e11e791e2c/commits/9f21737240
# https://github.com/specklesystems/speckle-examples/blob/main/python/speckle-py-starter/01_send_receive.py

client = SpeckleClient("https://speckle.xyz")
# Token generated in speckle user settings. Token is only allowed to "read" from streams. Not write
client.authenticate_with_token("7c501d41892aba1ed317b4191553c5223b9c3015c9")
# Connect to specle and get our "stream" for materials and their lamda values
def get_materials_from_speckle():
	print('get thermal conductivity from speckle')
	# Our materials document
	streamId = 'e11e791e2c'
	branch = client.branch.get(streamId, "main", 1)
	objHash = branch.commits.items[0].referencedObject
	received_base = client.object.get(streamId, objHash)
	data = received_base.data
	return data

# Connect to specle and get our "stream" for BR18.
def get_br18_from_speckle():
	print('get BR18 value from speckle')
	# Our BR18 document
	streamId = 'cce20ff6c3'
	branch = client.branch.get(streamId, "main", 1)
	objHash = branch.commits.items[0].referencedObject
	received_base = client.object.get(streamId, objHash)
	data = received_base.data
	return data

