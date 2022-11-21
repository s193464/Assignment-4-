import os.path
import webbrowser
# Make so we can get our information from the walls.py file
from walls import *

def writeHTML():
	# Much of the "write html" is borrowed from timms github
	# https://github.com/timmcginley/HTML-Build-IFC-Converter/blob/main/HTMLBuild.py

	'''
		write the HTML entities
	'''
	# parent directory - put in setting file?
	dir = "output/"
	# create an HTML file to write to
	if (os.path.exists("output/"))==False:
		# path = os.path.join(parent_dir, name)
		os.mkdir(dir)

	f_loc="output/index.html"
	f = open(f_loc, "w")
	cont=""

	# ---- START OF STANDARD HTML
	cont+=0*"\t"+"<HTML>\n"
	# ---- ADD HEAD
	cont+=1*"\t"+"<HEAD>\n"
	# ---- ADD HTMLBUILD CSS - COULD ADD OTHERS HERE :)
	cont+=2*"\t"+"<LINK rel='stylesheet' href='css/html-build.css'></LINK>\n"
	# ---- CLOSE HEAD
	cont+=1*"\t"+"</HEAD>\n"
	# ---- ADD BODY
	cont+=1*"\t"+"<BODY>\n"

	# ---- ADD CUSTOM HTML FOR THE BUILDING HERE
	cont+=writeCustomHTML()

	# ---- CLOSE BODY AND HTML ENTITIES
	cont+=1*"\t"+"</BODY>\n"
	cont+=0*"\t"+"</HTML>\n"

	# ---- WRITE IT OUT
	f.write(cont)
	f.close()

	# ---- TELL EVERYONE ABOUT IT
	print("\tSave    : "+f_loc)

	# We found out how to open the browser automaticly. I hope this makes Timm happy :)
	# https://elearning.wsldp.com/python3/python-open-web-browser/#:~:text=Python%20has%20a%20module%20called,browser%20with%20a%20given%20URL.
	# Find current folder on computer https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/
	browser_path = os.path.dirname(os.path.abspath(__file__))
	# print( browser_path + f_loc )
	webbrowser.open(browser_path + "/" + f_loc)

# Our html

def write_box_with_calculations():
	box = ""
	box+=2*"\t"+"<box>\n"
	box+=3*"\t"+""
	box+=2*"\t"+"</box>\n"

def write_box_with_u_value():
	box = ""
	box+=2*"\t"+"<box>\n"
	box+=3*"\t"+"<header>U-Value</header>\n"

	box+=3*"\t"+str(round(get_u_value(),2)) + "<unit>W/m<sup>2</sup> K</unit>\n"
	box+=2*"\t"+"</box>\n"
	return box

def write_box_br18():
	br18_valid = is_transmission_loss_br18_valid()

	if br18_valid :
		color = "green"
	else:
		color = "red"
	# We make the box green if the u-value is BR18 compliant, else its red
	box = ""
	box+=2*"\t"+"<box class=\""+color+"\">\n"
	box+=3*"\t"+"<header>BR18</header>\n"
	if br18_valid :
		box+=3*"\t"+"Yes"
	else:
		box+=3*"\t"+"No"

	box+=2*"\t"+"</box>\n"
	return box

def write_box_total_area():
	box = ""
	box+=2*"\t"+"<box>\n"
	box+=3*"\t"+"<header>Wall Area</header>\n"
	box+=3*"\t"+str(round(get_total_wall_area(),2)) + "<unit>m<sup>2</sup></unit>\n"
	box+=2*"\t"+"</box>\n"
	return box
def write_box_transmission():
	box = ""
	box+=2*"\t"+"<box>\n"
	box+=3*"\t"+"<header>Transmission loss</header>\n"
	box+=3*"\t"+str(round(get_transmission_loss(),2)) + "<unit>W</unit>\n"
	box+=2*"\t"+"</box>\n"
	return box


def writeCustomHTML():
	custom = ""
	custom += 2*"\t"+"<container>\n"
	# Box with u-value
	custom += write_box_with_u_value()
	# Box BR18
	custom += write_box_br18()
	# Box total area
	custom += write_box_total_area()
	# Box Transmission loss
	custom += write_box_transmission()
	custom += 2*"\t"+"</container>\n"
	return custom


