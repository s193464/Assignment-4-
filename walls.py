import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.pset

# Get all functions from our material helper file
from material_index import *
# Get our formels
from formels import *


# good links
# https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples
# https://ifcopenshell.github.io/docs/python/html/ifcopenshell-python/api-documentation.html
# https://thinkmoult.com/using-ifcopenshell-parse-ifc-files-python.html

print('Loading Duplex model')
modelDuplex = ifcopenshell.open('models/Duplex.ifc');
print( 'Finished loading Duplex model')

# We only need information about walls. so we find them by the IFCWALL type
walls = modelDuplex.by_type('IFCWALL')

#store our u values for the walls
u_value_data = []
external_wall_areas = []

for wall in walls:
	# https://standards.buildingsmart.org/IFC/DEV/IFC4_3/RC1/HTML/schema/ifcsharedbldgelements/lexical/ifcwall.htm

	# print ('--- New Wall ---')
	# print( wall.Name )
	# We have have found that area, and if the wall is an external wall, is available in the "ptets" data
	wall_property_sets = ifcopenshell.util.element.get_psets(wall)
	wall_is_external = wall_property_sets.get('Pset_WallCommon').get('IsExternal')
	# wall_area = wall_property_sets.get('PSet_Revit_Dimensions').get('Area')

	# print (wall_is_external)
	# print ( wall_area )

	# We only want to calculate for external walls
	if wall_is_external :
		# This might not be the best way - but in order to only look at real walls, and not foundation and similar, who also is "external", we check for the excact name
		if wall.Name.startswith('Basic Wall:Exterior - Brick on Block'):
			print('---')
			print('New wall')

			# Since the area is available via Revit Dimensions, we use those. We have validated by looking in blender, that the area is without windows
			wall_area = wall_property_sets.get('PSet_Revit_Dimensions').get('Area')
			external_wall_areas.append(wall_area)


			# Find the references for the wall
			# In the github - look where timm finds his materials
			# https://github.com/timmcginley/41934/blob/main/Example%20files/Python/get_properties.py
			# https://community.osarch.org/discussion/510/ifcopenshell-get-wall-layers-and-materials
			for associated_materials in wall.HasAssociations:
				#print ('Find thermal conductivity')
				# print(relAssociatesMaterial.RelatingMaterial)
				material_layers = associated_materials.RelatingMaterial.ForLayerSet.MaterialLayers
				u_value = calculate_u_value( material_layers )
				u_value_data.append(u_value)
				print(material_layers)
				# print ( "      Wall %s has a U value of: %s"%(wall.Name, u_value) )
				
				# Instead of handling each layer, it was easier to send them to our u-value formula
				for material_layer in material_layers :
					# Now we can find the size of each layer
					# print (material_layer.Material)
					print ( "      %s is %s m"%(material_layer.Material.Name,material_layer.LayerThickness) )


def get_u_value():
	print("U-value is %s W/m2*K"%(max(u_value_data)))
	# in case our u-values is different we use the highest
	return max(u_value_data)

def get_total_wall_area():
	print("Total wall area is %s m2"%(sum( external_wall_areas )))
	# get the total of our walls areas
	return sum( external_wall_areas )

def get_transmission_loss():
	external_wall_area = get_total_wall_area()
	u_value = get_u_value()
	transmission_loss_value = calculate_transmission_loss( external_wall_area, u_value )
	print("Transmission loss is %s W"%(transmission_loss_value))
	return transmission_loss_value

def is_transmission_loss_br18_valid() :
	u_value = get_u_value()
	br18 = get_br18_value()
	if u_value <= br18 :
		return True
	else:
		return False


