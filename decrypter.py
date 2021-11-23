# -*- coding: utf-8 -*-
'''Decrypts all encrypted files (with enigmer) in an input folder. Must be called with the salting string.
The  decrypted files are generated in the folder "decrypted".

Example: 
        python decrypter.py 'C:/Users/aaaa/Documents/encrypted/' '2021-10-21'

Python 3.x
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from datetime import datetime
import builtins
from sys import argv, stderr
from os import path, listdir

from srcs.filesUtils import obtainPass, convertFile2bytes, isExtension, saveBytes
from srcs.cryptoUtils import convertPass2key, decrypt

#---- definicions
outputFolder = './decrypted/'
extension = '.tzt'  # the file extension of the encripted data


def print(*args, **kwargs):
    # "decorating" print
    builtins.print(datetime.now(), '::: ', *args, **kwargs)


def showHelp(e: Exception):
    '''Prints a message for help
    ############################################### '''

    print('Error:', e, file=stderr)
    print('''DESCRIPTION:
    \t\tDecrypts files, encrypted with enigmer, in given <path> with <salt>.
    \t\tIt will request user password. It will decrypt even if <salt> or password are incorrect,
    \t\tbut files will be corrupted.

    \t\tUSAGE: decrypter <path> <salt>
    
    \t\tFor example:
    \t\t> decrypter . 2021-10-21
    
    ''')
    return


def main():
    '''
    
    ############################################### '''
    # ---
    try:
        args = argv[1:]
        srcPath, salt = args
    except Exception as e:
        showHelp(e)
        exit(1)

    # --- validating the path
    if not path.isdir(srcPath):
        showHelp(Exception('path --{}-- not found.'.format(srcPath)))
        exit(1)

    # --- from password to key
    password = obtainPass()
    key, iv = convertPass2key(password, salt)

    # --- loop by file
    files = listdir(srcPath)
    for idx, filename in enumerate(files):

        # ignoring folders
        if path.isdir(srcPath + '/' + filename):
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
