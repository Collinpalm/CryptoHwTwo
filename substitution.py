import sys
import re 

"""
run this on the command line with the text to be decrypted

"""
plainfreq = ({'a':.082},{'b':.015},{'c':.028},{'d':.043},{'e':.127},{'f':.022},{'g':.02},{'h':.061},{'i':.07},{'j':.002},{'k':.008},{'l':.04},{'m':.024},{'n':.067},{'o':.075},{'p':.019},{'q':.001},{'r':.06},{'s':.063},{'t':.091},{'u':.028},{'v':.01},{'w':.023},{'x':.001},{'y':.02},{'z':.001})
digrams = ['th', 'he', 'in', 'in', 'er', 'an', 're', 'ed', 'on', 'es', 'st', 'en', 'at', 'to', 'nt', 'ha', 'nd', 'ou', 'ea', 'ng', 'as', 'or', 'ti', 'is', 'et', 'it', 'ar', 'te', 'se', 'hi', 'of']
trigrams = ['the', 'ing', 'and', 'her', 'ere', 'ent', 'tha', 'nth', 'was', 'eth', 'for', 'dth']
#code from one of my old projects, IDK its origins
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def keytry(ciphertext, key):
    i = 0

def freqdecipher(charfreq, didict, tridict, doubledict):
    i = 0

def decrypt():
    ciphertext = sys.argv[1]
    characterfreq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    didict = {}
    tridict = {}
    doubledict = {}
    characterfreq[ord(ciphertext[0])-97] += 1
    characterfreq[ord(ciphertext[1])-97] += 1
    
    if (ciphertext[0] == ciphertext[1]):
        str = ciphertext[0] + ciphertext[1]
        if str in doubledict:
            doubledict.update({str: (doubledict[str] + 1)})
        else:
            doubledict.update({str: 1})
    
    didict.update({ciphertext[:2], 1})
    for element in range(2, len(ciphertext)):
        distr = ciphertext[element] + ciphertext[element-1]
        tristr = ciphertext[element] + ciphertext[element-1] + ciphertext[element-2]

        characterfreq[ord(ciphertext[element])-97] += 1
                
        if distr in didict:
            didict.update({distr: (didict[distr] + 1)})
        else:
            didict.update({distr: 1})
        
        if tristr in tridict:
            tridict.update({tristr: tridict[tristr] + 1})
        else:
            tridict.update({tristr: 1})

        if (ciphertext[element] == ciphertext[element-1]):
            str = ciphertext[element] + ciphertext[element-1]
            if str in doubledict:
                doubledict.update({str: (doubledict[str] + 1)})
            else:
                doubledict.update({str: 1})
    freqdecipher(characterfreq, didict, tridict, doubledict)
        
    
    







if __name__ == "__main__":
    decrypt()



