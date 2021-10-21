# -*- coding: utf-8 -*-
'''Decrypts all files in a folder.

Python 3.x
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from datetime import datetime
import builtins
from sys import argv
import os

from srcs.filesUtils import obtainPass, convertFile2bytes, isExtension, saveBytes
from srcs.cryptoUtils import convertPass2key, decrypt

#---- definicions
outputFolder = './decrypted/'
extension = '.tzt'  # the file extension of the encripted data


def print(*args, **kwargs):
    # "decorating" print
    builtins.print(datetime.now(), '::: ', *args, **kwargs)

def main():
    '''
    
    ############################################### '''
    # --- 
    args = argv[1:]
    srcPath, salt = args

    # --- validating the path
    if not os.path.isdir(srcPath):
        raise Exception('Input path incorrect.')

    # --- from password to key
    password = obtainPass()
    key, iv = convertPass2key(password, salt)

    # --- loop by file
    files = os.listdir(srcPath)
    for idx, filename in enumerate(files):

        # ignoring folders
        if os.path.isdir(srcPath + '/' + filename):
            print('{}/{} folder, not encrypting \t{}'.format(idx,
                                                             len(files) - 1, filename))
            continue
        
        # ignoring not decrypted files
        flag, originalname = isExtension(filename, extension)
        if flag:
            print('{}/{} Decrypting \t{}'.format(idx, len(files) - 1, filename))
        else:
            print('{}/{} Not encrypted \t{}'.format(idx, len(files) - 1, filename))
            continue

        fullName = srcPath + '/' + filename

        # --- Encryption
        cypherData = convertFile2bytes(fullName)
        data = decrypt(cypherData, key, iv)

        saveBytes(srcPath + '/'+outputFolder, originalname, data)

    return


if __name__ == "__main__":
    main()
