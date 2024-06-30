import os
import shutil

output_directory = '/kaggle/working'
saved_models_directory = os.path.join(output_directory, 'saved_models')

# List all files in the output directory
files = os.listdir(output_directory)


# Delete each file in the output directory
for file in files:
    file_path = os.path.join(output_directory, file)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path) and file != 'saved_models':
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'Failed to delete {file}. Reason: {e}')
        
# Delete each file in the saved_models directory
if os.path.exists(saved_models_directory):
    saved_model_files = os.listdir(saved_models_directory)
    for file in saved_model_files:
        file_path = os.path.join(saved_models_directory, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file}. Reason: {e}')

print("All files in the output and saved_models directories have been cleared.")
