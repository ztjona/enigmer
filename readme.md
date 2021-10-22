# Enigmer
## Description
Python functions to **encrypt** and **decrypt** files in a given folder using AES and a user password.

## Execution
### Encrypting
```
python enigmer.py 'C:/Users/uuuuu/Documents/'

```
It will require a user to input a password.
And will encrypt the files inside a folder called */encrypted/*.
It also generates a *salt.txt* file with the salting string required to decrypt.

#### Notes
* The salt string is the date when the encrpytion was carried on. Following this format: *2021-10-21*.
* It does not delete the original files.

### Decrypting
```
python decrypter.py 'C:/Users/uuuuu/Documents/encrypted/' '2021-10-21'

```
It will require the user to input a password.
And will decrypt the files inside a folder called */decrypted/*.

#### Notes
* It will decrypt even when the password and salt string are incorrect. Doing so will result in corrupted files.


