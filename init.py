import os
import kagglehub
import shutil

# 1. Dynamically detect the project root directory
base_dir = os.path.abspath(os.getcwd())
if os.path.basename(base_dir) == 'notebooks':
    base_dir = os.path.dirname(base_dir)

# 2. Define the exact professional project folder structure
project_structure = [
    os.path.join(base_dir, 'charts'),
    os.path.join(base_dir, 'data', 'raw'),
    os.path.join(base_dir, 'data', 'processed'),
    os.path.join(base_dir, 'docs', 'assets', 'skills_logos'),  # Updated to match your actual structure
    os.path.join(base_dir, 'notebooks')
]

# Create each folder and place an invisible .gitkeep file safely
for folder in project_structure:
    os.makedirs(folder, exist_ok=True)
    
    # Create the .gitkeep file only in data and charts folders to preserve them in Git
    if 'data' in folder or 'charts' in folder or 'skills_logos' in folder:
        gitkeep_path = os.path.join(folder, '.gitkeep')
        if not os.path.exists(gitkeep_path):
            with open(gitkeep_path, 'w') as f:
                pass  # Safely creates an empty file without overwriting anything
                
    print(f"Directory verified: {os.path.relpath(folder, base_dir)}")

# 3. Define the destination for raw data and proceed with the download
raw_destination = os.path.join(base_dir, 'data', 'raw')

print("\nDownloading dataset from Kaggle...")
temp_path = kagglehub.dataset_download("arshkon/linkedin-job-postings")

# 4. SAFE MERGE: Copy and overwrite files individually from cache to data/raw/
print(f"Organizing and merging files into: {os.path.relpath(raw_destination, base_dir)}")

# Helper function to walk through the cached data and copy files non-destructively
def safe_dir_copy(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        # Calculate the relative path from the source root
        rel_path = os.path.relpath(root, src_dir)
        target_folder = dest_dir if rel_path == "." else os.path.join(dest_dir, rel_path)
        
        # Ensure subdirectories exist without erasing existing ones
        os.makedirs(target_folder, exist_ok=True)
        
        # Copy files one by one (overwriting older versions but preserving custom files)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_folder, file)
            shutil.copy2(src_file, dest_file)

# Execute the safe merge function
safe_dir_copy(temp_path, raw_destination)

print("\nAll set! The LinkedIn Job Postings dataset is now perfectly integrated into your 'data/raw/' folder.")