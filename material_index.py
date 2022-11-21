from speckle_connect import *

# We define a method to get values for materials.
# Later this was changed to call specle, and return the values from them.
speckle_materials = get_materials_from_speckle()
materials = {}
# Since our code first was made with the lamda values directly in here, we need to convert the format we get from speckle, to match our format, so we dont have to rewrite too much code
for speckle_material in speckle_materials:
	print ( "%s is %s W/m*K"%(speckle_material['Material'],speckle_material['Thermal conductivity']))
	materials[ speckle_material['Material'] ] = speckle_material['Thermal conductivity']
	# old code
	# name : lambda value
	# materials = {
	# 	'Masonry - Brick' : 0.7,
	# 	'Misc. Air Layers - Air Space' : 0.025,
	# 	'Insulation / Thermal Barriers - Rigid insulation' : 0.039,
	# 	'Masonry - Concrete Block' : 1.4,
	# 	'Metal - Stud Layer' : 0.05,
	# 	'Plasterboard' : 0.25,
	# }
	#print( materials )
	

# Get the lamda value for the material
def get_material_lambda(material):

	# materials = get_materials()
	return materials.get( material )

def get_br18_value():
	# br18 = 0.30
	br18_speckle = get_br18_from_speckle()
	# The value, is in the first row
	br18 = br18_speckle[0]["BR18"]
	print("BR18 value is %s W/m2*K"%(br18))
	return br18

