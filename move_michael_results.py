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

def main():
	n_cases=20
	case_folder_names=[]
	case_file_names=[]
	for case in range(1, n_cases+1):
		case_folder_name="case_"+str(case)
		case_folder_names=case_folder_names+[case_folder_name]
		case_file_name='hm50_finite_case_'+str(case)
		case_file_names=case_file_names+[case_file_name]
	print(case_folder_names)
	print(case_file_names)

	#Define the location of the originial files
	old_files_location='/global/scratch/lpgregg/burnup_safety/michael_rerun'

	#Define the location for the perturbed temperature files
	new_files_location='/global/scratch/lpgregg/burnup_safety/michael_rerun_results'

	#copy over all the input files.
	results_filename="hm50_finite_input_res.m"
	depletion_filename="hm50_finite_input_dep.m"

	for i in range(0,len(case_folder_names)):
		mkdir_p(new_files_location);
		mkdir_p(new_files_location+"/"+case_folder_names[i])
		case_folder_names[i]
		
		old_file_path=old_files_location+"/"+case_folder_names[i]+"/"+results_filename
		new_file_path=new_files_location+"/"+case_folder_names[i]+"/"+results_filename
		print(old_file_path)
		print(new_file_path)

		copyfile(old_file_path,
			new_file_path)

		old_file_path=old_files_location+"/"+case_folder_names[i]+"/"+depletion_filename
		new_file_path=new_files_location+"/"+case_folder_names[i]+"/"+depletion_filename
		print(old_file_path)
		print(new_file_path)

		copyfile(old_file_path,
			new_file_path)		


main()
