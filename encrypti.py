import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file: 
        content = file.read();
    fernet = Fernet(key);
    encrypt_content = fernet.encrypt(content)
    with open(file_path, "wb") as file:
        file.write(encrypt_content)

def encrypt_files_in_folder(folder_path, key):
    for root, dils, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

key = Fernet.generate_key();
#Passe o diretorio na variável folder_path
folder_path ="";

encrypt_files_in_folder(folder_path, key)

with open('key.key', 'wb') as key_file:
    key_file.write(key)

    