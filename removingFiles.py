# importing the required modules
import os
import shutil
import time

# main function
def main():

	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	# specify the days
	days = 30

	# converting days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# comparing the days
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folder
				

				# breaking after removing the root_folder
				break

			else:

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the days
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function

						# incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						
						# incrementing count

		else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= get_file_or_folder_age(path):

				# invoking the file
				
				
				# incrementing count

	else:

		# file/folder is not found
		

		# incrementing count

	


def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message, use print
		

	else:

		# failure message,use print
		



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message, use print
		

	else:

		# failure message, use print
		


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	

	# returning the time
	


if __name__ == '__main__':
	main()
