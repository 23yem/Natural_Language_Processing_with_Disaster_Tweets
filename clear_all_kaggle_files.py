import os
import shutil

output_directory = '/kaggle/working'
directory_name = 'saved_models' # change this to whatever directory you need to clear

directory = os.path.join(output_directory, directory_name)

# List all files in the output directory
files = os.listdir(output_directory)

# Delete each file in the output directory
for file in files:
    file_path = os.path.join(output_directory, file)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path) and file != directory_name: 
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'Failed to delete {file}. Reason: {e}')
        
# Delete each file in the directory_name directory
if os.path.exists(directory):
    saved_model_files = os.listdir(directory)
    for file in saved_model_files:
        file_path = os.path.join(directory, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file}. Reason: {e}')

print("All files in the output and directory have been cleared.")
