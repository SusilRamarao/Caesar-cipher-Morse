import caesar

from __main__ import *

msg = caesar.caesar
print msg
print "Generating morse code"

print "Enter the message you want to convert"


alpha = {' ':' ', 'a' : '.-' , 'b' : '-...','c' : '-.-.','d' : '-..','e':'.', 'f' :'..-.','g':'--.', 'h' : '....', 'i': '..', 'j' : '.---',
          'j' : '.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-',
          'r':'.-.','s':'...','t':'-','u':'..-','v':'...-',
          'w':'.--','x':'-..-','y':'-.--','z':'--..'}
numbers = {'0' :'-----','1' : '.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---.','9':'----.','.':'.-.-.-',',':'--..--','?':'..--..'}          

for i in range(len(msg)):
	cur = msg[i]
	if cur.isdigit():
		print numbers[cur]

	else:
		print alpha[cur]






	
