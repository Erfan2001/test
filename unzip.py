import zipfile


with zipfile.ZipFile("Folder1.zip","r") as zip_ref:
    zip_ref.extractall()