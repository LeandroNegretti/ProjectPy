import os
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file: 
        content = file.read();
    fernet = Fernet(key);
    decrypt_content = fernet.decrypt(content)
    with open(file_path, "wb") as file:
        file.write(decrypt_content)

def decrypt_files_in_folder(folder_path, key):
    for root, dils, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

with open("key.key", "rb") as key_file:
    key= key_file.read()
#Passe o diretorio na variável folder_path
folder_path ="";

decrypt_files_in_folder(folder_path, key)
