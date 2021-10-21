# -*- coding: utf-8 -*-
'''Library with functions for the encryption part.

Python 3.x
21 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES


def convertPass2key(password: str, salt: str, keyLen: int = 32, ivLen: int = 16) -> tuple[bytes, bytes]:
    '''Returns the ``key`` and ``iv`` generated from a password and a salting string.

    ############################################### '''

    # Your key that you can encrypt with
    saltB = bytes(salt, 'UTF-8')
    kv = PBKDF2(password, saltB, dkLen=keyLen + ivLen)  # key and vi
    key = kv[:keyLen]
    iv = kv[keyLen:]

    return key, iv


def encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    '''Do the encryption with the given key and data.
    Returns the bytes of the encription.

    ############################################### '''

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)  # CFB mode
    ciphered_data = cipher.encrypt(data)

    return ciphered_data


def decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    '''Do the decryption with the given key and data.
    Returns the bytes of the decription.

    ############################################### '''

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)  # CFB mode
    ciphered_data = cipher.decrypt(data)

    return ciphered_data
