# -*- coding: utf-8 -*-
'''Encrypts all the files in a given directory.
It ask for a password that is used to generate the AES key.
The key is generated from password with PBKDF2, and salted with the date of the encription.


Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from datetime import datetime
from datetime import date
from sys import argv
import os

from srcs.cryptoUtils import convertPass2key, encrypt
from srcs.filesUtils import convertFile2bytes, saveBytes

from getpass import getpass

extension = '.tzt' # the file extension of the encripted data
folder= './encrypted/'

def obtainPass() -> str:
    '''Returns the validated password from the user.
    ############################################### '''

    while True:

        passA = getpass(prompt="Ingrese su contraseña:")
        passB = getpass(prompt="Reingrese la misma contraseña:")

        if passA == passB:
            break
        print('Contraseñas no coinciden. Intente nuevamente.')

    return passB


def getSaltStr() -> str:
    '''Returns a string for salting and saves it in a salt.txt file. By default is the date.
    
    For example:
        '2021-10-21'
    ############################################### '''

    salt = datetime.now().strftime('%Y-%M-%d')
    with open('salt.txt', 'w') as txt:
        print(salt)
    return salt


def main():
    '''
    ############################################### '''
    # --- validating path

    args = argv[1:]
    path, = args

    # --- validating the path
    if not os.path.isdir(path):
        raise Exception('Input path incorrect.')

    # --- from password to key
    password = obtainPass()
    salt = getSaltStr()
    key, iv = convertPass2key(password, salt)

    # --- from password to key
    files = os.listdir(path)
    for idx, filename in enumerate(files):
        if os.path.isdir(filename):
            continue

        print('{}/{} Encrypting \t{}'.format(idx, len(files), filename))
        
        data = convertFile2bytes(filename)
        cypherData = encrypt(data, key, iv)

        saveBytes(folder, filename + extension, cypherData)


    return


if __name__ == "__main__":
    main()
