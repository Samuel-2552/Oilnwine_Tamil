import os
path="TamilReading"
files = os.listdir(path)

for file in files:
    old_name = os.path.join(path, file)
    # Set the path to the file
    file_path = old_name

    # Open the file in append mode
    with open(file_path, 'a') as f:
    # Write the line of text to the file
        f.write('Tamil O.V. Bible - பரிசுத்த வேதாகமம் O.V.')