#import 
import ifcopenshell 
import ifcopenshell.util.element 

#import IFC files
modelDuplex = ifcopenshell.open('models/Duplex.ifc')
walls = (modelDuplex.by_type('IfcWall'))

#Get material
wall = (modelDuplex.by_id('2O2Fr$t4X7Zf8NOew3FNqI'))
print(wall)

wall_property_sets = ifcopenshell.util.element.get_psets(wall)
print(wall_property_sets)
wall_type = wall_property_sets.get('Pset_WallCommon').get('Reference')
print('---')
print(wall_type)

wall_is_external = wall_property_sets.get('Pset_WallCommon').get('IsExternal')

print('----')
print(wall_is_external)




beams = modelDuplex.by_type("IfcBeam")
for beam in beams:
    for relAssociatesMaterial in beam.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)






material_layer_sets = modelDuplex.by_type('IFCMATERIALLAYERSET')
for material_layer_set in material_layer_sets:
	material_layer_sets_name = material_layer_set.LayerSetName
print(material_layer_set)

def get_materiallayer_set_usage():
    for product in products:
        if product.HasAssociations:
            for i in product.HasAssociations:
                if i.is_a('IfcRelAssociatesMaterial'):
                    for materials in i.RelatingMaterial:
                        if (type(materials)) is tuple:
                            for material in materials:
                                print (product.Name, material.Material, material.LayerThickness)


#Get thickness of each material

#import thermal conductivity from speckle

#calculate U-values

#check with BR18 - does the U-value correspond with BR18?


#get area of the exterior walls

#calculate transmission loss


#show results in HTML 
