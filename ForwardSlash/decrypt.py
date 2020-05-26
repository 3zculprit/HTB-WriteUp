def decrypt(key, msg):
    key = list(key)
    msg = list(msg)	
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)


with open("ciphertext",'rb') as f:
	 msg = f.read().rstrip()
#print (msg)
#with  open("first-r.txt","r") as ry:
#	keys = ry.readlines()
#count = 1
#for key in keys:
#	d_key = key.rstrip()
#	try:
#		result = decrypt(d_key,msg)
#		with open("list.txt","a+") as l:
#			l.write(str(count)+":"+result)
#		count +=1
#	except UnicodeDecodeError:
#		continue


key = "teamareporsiempre"
print decrypt(key,msg)
