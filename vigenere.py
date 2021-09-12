import sys
import re 

"""
run this on the command line with the text to be decrypted

"""
#I found slightly more accurate numbers, I used them bc I wanted a closer approximation
english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def freq_analysis(sequence):
	all_chi_squareds = [0] * 26
	for i in range(26):
		chi_squared_sum = 0.0
		sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26
		for l in sequence_offset:
			v[ord(l) - ord('a')] += 1
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))
		for j in range(26):
			chi_squared_sum+=((v[j] - float(english_frequences[j]))**2)/float(english_frequences[j])
		all_chi_squareds[i] = chi_squared_sum
	shift = all_chi_squareds.index(min(all_chi_squareds))
	return chr(shift+97)


def getioc(cipher):
	#according to stack overflow you need to do it this way
	#I wanted to only get the len at the begining and then continue
	#to use it throughout the program as a variable, but NOOO
	#theres like rules and crap
	N = float(len(cipher))
	frequency_sum = 0.0
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		frequency_sum+= cipher.count(letter) * (cipher.count(letter)-1)

	ic = frequency_sum/(N*(N-1))
	return ic


def getKey(ciphertext):
	ic_table=[]
	for guess_len in range(26):
		ic_sum=0.0
		avg_ic=0.0
		for i in range(guess_len):
			sequence=""
			for j in range(0, len(ciphertext[i:]), guess_len):
				sequence += ciphertext[i+j]
			ic_sum+=getioc(sequence)
		if not guess_len==0:
			avg_ic=ic_sum/guess_len
		ic_table.append(avg_ic)

	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])

	if best_guess % second_best_guess == 0:
		keylength = second_best_guess
	else:
		keylength = best_guess
	key = ''
	for i in range(keylength):
		sequence=""
		for j in range(0,len(ciphertext[i:]), keylength):
			sequence+=ciphertext[i+j]
		key+=freq_analysis(sequence)

	return key


def decrypt(ciphertext, key):
	cipherAscii = [ord(letter) for letter in ciphertext]
	keyAscii = [ord(letter) for letter in key]
	plainAscii = []
	for i in range(len(cipherAscii)):
		plainAscii.append(((cipherAscii[i]-keyAscii[i % len(key)]) % 26) +97)
	plaintext = ''.join(chr(i) for i in plainAscii)
	print(plaintext)

def main():
	ciphertext = sys.argv[1]
	keylen = getKey(ciphertext)
	decrypt(ciphertext, keylen)







if __name__ == "__main__":
    main()