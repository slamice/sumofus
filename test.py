def buildCodeBook():
	letters ='.abcdefghijklnopqrstuvwxyz '
	codeBook = {}
	key = 0
	for c in letters:
		codeBook[key] = c
		key += 1
	return codeBook
 
def decode(cypherText, codeBook):
	plainText = ''
	for e in cypherText:
		if e in codeBook:
		  plainText += codeBook[e]
		else:
		  plainText += ' '
	return plainText
 
codeBook = buildCodeBook()
msg = (8,14,12,1)
print decode(msg, codeBook)
