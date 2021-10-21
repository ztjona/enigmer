# -*- coding: utf-8 -*-
'''Utils to handle files in the proyect.

Python 3.x
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''


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


def saveBytes(folder: str, filename: str, data: bytes):
    '''Saves the given ``data`` bytes in the ``filename`` inside the ``folder``.

    ############################################### '''
    if not path.isdir(folder):
        mkdir(folder)

    with open(folder +'/' + filename, "wb") as fileOut:
        fileOut.write(data)


# convertFile2bytes('a.txt')
# convertFile2bytes('b.JPG')
