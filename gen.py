import os

# Base directory for the project
base_dir = 'src'

# Number of files per folder
files_per_folder = 1000

# Total number of files
total_files = 20000

# Create base directory if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Generate the files
for i in range(total_files):
    folder_index = i // files_per_folder + 1
    file_index = i + 1
    folder_name = f'folder{folder_index}'
    file_name = f'Component{file_index}.tsx'
    
    folder_path = os.path.join(base_dir, folder_name)
    file_path = os.path.join(folder_path, file_name)
    
    # Create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Write the TypeScript file
    with open(file_path, 'w') as f:
        f.write(f"""import React from 'react';
import BaseComponent from '../BaseComponent';

const Component{file_index} = () => <div>{file_index}</div>;

export default Component{file_index};
""")

print("Files generated successfully.")