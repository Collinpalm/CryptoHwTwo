import sys
import re 

"""
run this on the command line with the text to be decrypted

"""
triedKeys = []


#code from one of my old projects, IDK its origins
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def findSubStrings(cipher, keylen):
    subStrings = {}
    str = ""

    for x in range(keylen-1, len(cipher)):
        for element in range(0, keylen-1):
            str += cipher[element]
        if str in subStrings:
            subStrings.update({str: (subStrings[str]+1)})
        else:
            subStrings[str] = 1
        str = ""

def decrypt():
    ciphertext = sys.argv[1]
    
    







if __name__ == "__main__":
    decrypt()