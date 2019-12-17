
f=open("/home/robert/check.txt",'r',encoding='UTF-8')
print (''.join(format(i, 'b') for i in bytearray(f.read(), encoding ='utf-8')))

f1=open("/home/robert/out.txt",'r',encoding='UTF-8')
print (''.join(format(i, 'b') for i in bytearray(f1.read(), encoding ='utf-8')))

f2=open("/home/robert/passwordreminder.txt",'r',encoding='UTF-8')
print (''.join(format(i, 'b') for i in bytearray(f2.read(), encoding ='utf-8')))
