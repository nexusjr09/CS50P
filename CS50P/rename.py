import os
import re

# The directory containing the files ('.' means the current directory)
directory = "."

# Loop through all files in the current directory
for filename in os.listdir(directory):
    # Check if the file is a Python file and starts with a digit followed by text
    if filename.endswith(".py") and re.match(r"^\d+", filename):

        # Use re.sub to remove the leading digits and any non-alphabetic/non-underscore characters
        # right after the number (e.g., '15' or '15_')
        new_filename = re.sub(r"^\d+[_]*", "", filename)

        # Full paths for renaming
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        # Check if a file with the new name already exists to prevent errors
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped: {filename} -> {new_filename} (New name already exists)")

print("\nRenaming complete.")
