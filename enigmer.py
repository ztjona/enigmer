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

import builtins
from datetime import datetime
from sys import argv
import os

from srcs.cryptoUtils import convertPass2key, encrypt
from srcs.filesUtils import convertFile2bytes, saveBytes

from getpass import getpass

extension = '.tzt'  # the file extension of the encripted data
folder = './encrypted/'

# "decorating" print


def print(*args, **kwargs):
    builtins.print(datetime.now(), '::: ', *args, **kwargs)


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

    salt = datetime.now().strftime('%Y-%m-%d')
    with open('salt.txt', 'w') as file:
        file.write(salt)
    print('salting is:\t\t', salt)
    return salt


def main():
    '''
    ############################################### '''
    # --- validating path

    args = argv[1:]
    srcPath, = args

    # --- validating the path
    if not os.path.isdir(srcPath):
        raise Exception('Input path incorrect.')

    # --- from password to key
    password = obtainPass()
    salt = getSaltStr()
    key, iv = convertPass2key(password, salt)

    # --- from password to key
    files = os.listdir(srcPath)
    for idx, filename in enumerate(files):
        if os.path.isdir(filename):
            print('{}/{} folder, not encrypting \t{}'.format(idx,
                                                             len(files) - 1, filename))
            continue

        print('{}/{} Encrypting \t{}'.format(idx, len(files) - 1, filename))

        data = convertFile2bytes(srcPath + '/' + filename)
        cypherData = encrypt(data, key, iv)

        saveBytes(srcPath + '/'+folder, filename + extension, cypherData)

    return


if __name__ == "__main__":
    main()
