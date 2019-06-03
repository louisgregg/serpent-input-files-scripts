#!/usr/bin/python
import os, sys
from shutil import copyfile
import errno
# import numpy as np

# def temp_perturbation(density_0, T_0_C, T_perturbation_C):
# 	a=4.4738;
# 	b=0.9304E-03;
# 	kelvin=273.15;
# 	T_0_K=T_0_C+kelvin;
# 	atomic_density_array = atomic_density_0 * (a - b*T_array_K)/(a - b*T_0_K);	
# 	return atomic_density_array


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

def main():
	n_cases=20
	case_folder_names=[]	
	for case in range(1, n_cases+1):
		case_folder_name="case_"+str(case)
		case_folder_names=case_folder_names+[case_folder_name]
	print(case_folder_names)


	radius_folder_names=[]
	r_core=[150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
	for radius in r_core:
		radius_folder_name="r_core_"+str(radius)
		radius_folder_names=radius_folder_names+[radius_folder_name]
	print(radius_folder_names)


	#Define the location of the originial files
	old_files_location='./serpent_cases'

	#Define the location for the perturbed temperature files
	new_files_location='./serpent_cases_analysis_3'

	#copy over all the input files.
	# geometry_filename="BNB_MCFR_1_geometry"
	# materials_filename="BNB_MCFR_1_materials"
	results_filename="BNB_MCFR_1_input_res.m"
	depletion_filename="BNB_MCFR_1_input_dep.m"
	for case_folder in case_folder_names:
		for radius_folder in radius_folder_names:
			mkdir_p(new_files_location);
			mkdir_p(new_files_location+"/"+case_folder)
			mkdir_p(new_files_location+"/"+case_folder+"/"+radius_folder)

			# copyfile(old_files_location+"/"+case_folder+"/"+radius_folder+"/"+geometry_filename,
			# 	new_files_location+"/"+case_folder+"/"+radius_folder+"/"+geometry_filename)
			copyfile(old_files_location+"/"+case_folder+"/"+radius_folder+"/"+depletion_filename,
				new_files_location+"/"+case_folder+"/"+radius_folder+"/"+depletion_filename)
			copyfile(old_files_location+"/"+case_folder+"/"+radius_folder+"/"+results_filename,
				new_files_location+"/"+case_folder+"/"+radius_folder+"/"+results_filename)



main()
# T_0_C=900;
# kelvin=273.15;
# T_0_K=T_0_C+kelvin;
# delta_T=[10 50 100 200];
# atomic_density_0=0.027461600000000;
# a=4.4738;
# b=0.9304E-03;
# T_array_K=delta_T+T_0_K;
# atomic_density_array = atomic_density_0 .* (a - b*T_array_K)/(a - b*T_0_K);	
