

message = raw_input()
caesar = ""

key = 4

alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(message)):
	akey = 0
	j = 0
	if message[i] == " ":
		caesar = caesar + " "
		continue
	
	while message[i] != alpha[j]:
		j = j + 1

	while akey != key:
		j = j + 1
		if j > 25:
			j = 0
		akey = akey + 1

	caesar = caesar + alpha[j]

print caesar


