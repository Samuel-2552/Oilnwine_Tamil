import os
path="TamilReading"
files = os.listdir(path)

for file in files:
    old_name = os.path.join(path, file)
    # Set the path to the file
    file_path = old_name

    # Open the file and read the lines into a list
    with open(file_path, "rb") as f:
        lines = f.readlines()

    # Remove the first two and last two lines
    lines = lines[2:-4]

    # Write the modified lines back to the file
    with open(file_path, "wb") as f:
        f.writelines(lines)