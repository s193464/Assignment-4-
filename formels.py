from material_index import *

def calculate_u_value(material_layers):
	# u = 1/( 0.13 + SUM([d/l,d/l,...]) + 0.04)
	# Base values of R.
	r = 0.13 + 0.04
	# Find SUM() of the materials, where R is calculated for each material
	for material in material_layers:
		#  print ( "%s is %s m"%(material.Material.Name, material.LayerThickness) )
		r = r + calculate_r( material.LayerThickness, get_material_lambda( material.Material.Name ) )

	u_value= 1/r
	return u_value

def calculate_transmission_loss( area, u_value ):
	transimission_loss = u_value * area * (20-(-12))
	return transimission_loss

def calculate_r(thinkness,material_lambda_value):
	return thinkness/material_lambda_value
