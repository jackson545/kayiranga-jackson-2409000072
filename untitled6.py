# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zp5WzeWV4kETsy1BsBJPffsCkUK_K4FF
"""

!pip install cryptography

from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
message1 = "First name"
message2= "kayiranga"
encrypted_message1 = fernet.encrypt(message1.encode())
decrypted_message1 =fernet.decrypt(encrypted_message1)
encrypted_message2 = fernet.encrypt(message2.encode())
decrypted_message2 =fernet.decrypt(encrypted_message2)
print(decrypted_message1.decode())
print(decrypted_message2.decode())