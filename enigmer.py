# -*- coding: utf-8 -*-
'''Encrypts all the files in a given directory. The encrypted files are generated in a folder called "/encrypted/"
It ask for a password that is used to generate the AES key.
The key is generated from password with PBKDF2, and salted with the date of the encription.

Example:
    python enigmer.py 'C:/Users/uuuuu/Documents/'



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
from sys import argv, stderr
from os import path, listdir

from srcs.cryptoUtils import convertPass2key, encrypt
from srcs.filesUtils import convertFile2bytes, saveBytes, obtainPass

extension = '.tzt'  # the file extension of the encripted data
folder = './encrypted/'


def print(*args, **kwargs):
    # "decorating" print
    builtins.print(datetime.now(), '::: ', *args, **kwargs)


def getSaltStr() -> str:
    '''Returns a string for salting and saves it in a salt.txt file. By default is the date.
    
    For example:
        '2021-10-21'
    ############################################### '''

    salt = datetime.now().strftime('%Y-%m-%d')
    
    print('salting is:\t\t', salt)
    return salt


def showHelp(e:Exception):
    '''Prints a message for help
    ############################################### '''
    
    print('Error:', e, file=stderr)
    print('''DESCRIPTION:
    \t\tEncrypts files in given <path>.
    \t\tThe encription requires a password, and salts it with the current date.
    \t\tUSAGE: enigmer <path>
    \t\tFor example:
    \t\t> enigmer .
    
    ''')
    return


def main():
    '''
    ############################################### '''
    # --- input from command line
    try:
        args = argv[1:]
        srcPath, = args
    except Exception as e:
        showHelp(e)
        exit(1)


    # --- validating the path
    if not path.isdir(srcPath):
        showHelp(Exception('path --{}-- not found.'.format(srcPath)))
        exit(1)
        

    # --- from password to key
    password = obtainPass()
    salt = getSaltStr()
    key, iv = convertPass2key(password, salt)

    # --- loop by file
    files = listdir(srcPath)
    for idx, filename in enumerate(files):

        # ignoring folders
        if path.isdir(srcPath + '/' + filename):
            print('{}/{} folder, not encrypting \t{}'.format(idx,
                                                             len(files) - 1, filename))
            continue

        print('{}/{} Encrypting \t{}'.format(idx, len(files) - 1, filename))

        # --- Encryption
        data = convertFile2bytes(srcPath + '/' + filename)
        cypherData = encrypt(data, key, iv)

        saveBytes(srcPath + '/'+folder, filename + extension, cypherData)

    print('Saving salt')
    with open('salt.txt', 'w') as file:
        file.write(salt)
    print('Done!')
    
    return


if __name__ == "__main__":
    main()
