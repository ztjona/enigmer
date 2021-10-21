# -*- coding: utf-8 -*-
'''Utils to handle files in the proyect.

Python 3.x
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''


from getpass import getpass
from os import mkdir, path


def convertFile2bytes(filename: str) -> bytes:
    '''
    Returns a byte representation of a file.

    ############################################### '''
    with open(filename, 'rb') as fh:
        all_lines = fh.readlines()
    data = bytes('', 'UTF-8')
    dataB = data.join(all_lines)

    return dataB



def isExtension(filename:str, extension:str)->tuple[bool, str]:
    '''Returns true when the given ``filename`` is in the given ``extension``.
    
    ############################################### '''
    parts = filename.split(extension)
    if len(parts) == 2:
        rawName, rest = parts
        
        if not rest:
            # there is nothing after the extension! good.
            return True, rawName
        else:
            # there is something after the extension name.
            return False, ''
    else:
        return False, ''
        


def saveBytes(folder: str, filename: str, data: bytes):
    '''Saves the given ``data`` bytes in the ``filename`` inside the ``folder``.

    ############################################### '''
    if not path.isdir(folder):
        mkdir(folder)

    with open(folder + '/' + filename, "wb") as fileOut:
        fileOut.write(data)


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

# convertFile2bytes('a.txt')
# convertFile2bytes('b.JPG')
