import os

# Set the path to the folder containing the files you want to rename
path = "November"

# Get a list of the files in the folder
files = os.listdir(path)
i=1
# Iterate over the list of files
for file in files:
  # Compute the new file name
  new_name = file.replace(file, "11-"+str(i)+".pdf")
  i+=1
  # Use the os.rename() method to rename the file
  os.rename(os.path.join(path, file), os.path.join(path, new_name))