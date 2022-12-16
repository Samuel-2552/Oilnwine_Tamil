import aspose.words as aw
import os
path="TamilReading\January"
files = os.listdir(path)

for file in files:
    old_name = os.path.join(path, file)
    new_name = os.path.splitext(file)[0] + ".txt"
    #print(file,new_name)
    doc = aw.Document(old_name)
    doc.save(new_name)