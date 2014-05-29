def transcribe(s):
	'''given a string, replace each K with M, each O with Q, and each E with G.
	str --> str '''

	first = s.replace('k', 'm')
	second = first.replace ('o', 'q')
	third = second.replace('e', 'g')
	print third 


def add_two(s):
	'''to try to unscramble the string, I'm guessing shift each letter by 2 in the alphabet.
	str --> str

	>>>g fmnc wms
	I hope you

	'''
	alphabet ="abcdefghijklmnopqrstuvwxyz"
	translated = ""

	for i in s:
		if i in alphabet:
		    j = alphabet.find(i)
		    if j < len(alphabet)-2:		
		        newletter = alphabet[j+2]
			translated += newletter
		    elif j >= len(alphabet)-2:
			newletter = alphabet[26-j-2]
		        translated += newletter
		elif i not in alphabet:
		    translated += i

	print translated

add_two("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

add_two("map")


