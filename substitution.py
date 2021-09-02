import sys
import re 

"""
run this on the command line with the text to be decrypted

"""
#code from one of my old projects, IDK its origins
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


def decrypt():
    ciphertext = sys.argv[1]
    characterfreq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for element in range(0, len(ciphertext)):
        characterfreq[ord(ciphertext[element])-97] += 0
        
    
    







if __name__ == "__main__":
    decrypt()



