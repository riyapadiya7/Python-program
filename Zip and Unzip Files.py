import zipfile

# Zip file
with zipfile.ZipFile("test.zip", "w") as z:
    z.write("sample.txt")

print("File zipped")

# Unzip file
with zipfile.ZipFile("test.zip", "r") as z:
    z.extractall("extract_folder")

print("File unzipped")
