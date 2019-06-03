#!/usr/bin/python
import os, sys
import errno
from shutil import copyfile
import numpy as np
import math # for use of math.pi

### Define a modified folder 
### creator which doesn't throw an error if the fodler already exists.
### uses errno and os
### https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python 
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


#### Python equivalent of sed for file editing
# with open("/etc/apt/sources.list", "r") as sources:
#     lines = sources.readlines()
# with open("/etc/apt/sources.list", "w") as sources:
#     for line in lines:
#         sources.write(re.sub(r'^# deb', 'deb', line))


### Define folder name strings etc
template_folder="input_files_template"
geometry_filename="BNB_MCFR_1_geometry"
materials_filename="BNB_MCFR_1_materials"
input_filename="BNB_MCFR_1_input"

### Define geometry constants
dc_salt_thickness=20
plena_thickness=5
rpv_thickness=5
reflector_thickness=20
usi_thickness=20
lsi_thickness=20


### Define radii arrays
r_core=np.array([150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300])
core_power_watts=300*2*math.pi*(r_core**3) # total core power in watts. 
r_reflector = r_core+reflector_thickness
r_si=r_reflector
r_dc = r_reflector+dc_salt_thickness
r_rpv = r_dc+rpv_thickness

### Define top and bottom arrays
### All symmetric axially now so can define bottoms as -tops
top_core=r_core
bottom_core=-r_core

top_reflector=top_core
bottom_reflector=bottom_core

top_si=top_core+usi_thickness
bottom_si=bottom_core-lsi_thickness

top_dc=top_core+usi_thickness+plena_thickness
bottom_dc=bottom_core-lsi_thickness-plena_thickness

top_rpv=top_dc+rpv_thickness
bottom_rpv=bottom_dc-rpv_thickness

### Here's how we form the multi-d array of values
### https://stackoverflow.com/questions/21887754/numpy-concatenate-two-arrays-vertically
r_array=np.concatenate([r_core[None,:],r_reflector[None,:],r_si[None,:],r_dc[None,:],r_rpv[None,:]])
top_array=np.concatenate([top_core[None,:],top_reflector[None,:],top_si[None,:],top_dc[None,:],top_rpv[None,:]])
bottom_array=np.concatenate([bottom_core[None,:],bottom_reflector[None,:],bottom_si[None,:],bottom_dc[None,:],bottom_rpv[None,:]])

surface_names = ["core", "reflector", "si", "dc","rpv"]
surface_numbers = ["1", "4", "7", "5","6"]


#### Here calculate the volume of pure salt (excl. mixed regions) in the WHOLE CORE
volume_active_core = 2*math.pi*(r_core**3) 
volume_reflector=math.pi*(r_reflector**2)*(top_reflector-bottom_reflector) - volume_active_core
volume_si = math.pi*(r_si**2)*(top_si-bottom_si) - volume_active_core - volume_reflector
volume_all_salt=math.pi*(r_dc**2)*(top_dc-bottom_dc) - volume_si - volume_reflector

#print(volume_all_salt)

# #Define the location of the originial files
#files_location='./serpent_cases'
old_string='mat fuel  -3.38E+00 burn 1 vol 1'


# Create the folder names for each case.
n_cases=20
case_folder_names=[]	
for case in range(1, n_cases+1):
	case_folder_name="case_"+str(case)
	case_folder_names=case_folder_names+[case_folder_name]


# Create the folder names for each radius.
radius_folder_names=[]
for radius in r_core:
	radius_folder_name="r_core_"+str(radius)
	radius_folder_names=radius_folder_names+[radius_folder_name]





for case_folder in case_folder_names:
	#for radius_folder in radius_folder_names:
	for i in xrange(0,len(radius_folder_names)):
		radius_folder=radius_folder_names[i]

		# Define the input folder path
		path_to_file="./"+case_folder+"/"+radius_folder+"/"+materials_filename
		print(path_to_file)

		#define the new fuel definition including correct volume. 
		new_string='mat fuel  -3.38E+00 burn 1 vol '+str(volume_all_salt[i])
		print(new_string)
		## Open the relevant geometry file to edit
		#### Python equivalent of sed for file editing
		# with open(path_to_file, "r") as sources:
		#     lines = sources.readlines()
		# with open(path_to_file, "w") as sources:
		#     for line in lines:
		#     	sources.write(line.replace(old_string,new_string))

#print(volume_all_salt(5))
# print(volume_active_core[None,5])
# print(volume_reflector[None,5])
# print(volume_si[None,5])
# print(volume_all_salt[None,5])