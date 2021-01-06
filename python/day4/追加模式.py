f=open("list","a+") #a+能读，能写，但是指向的是尾部
f.write("4")

print(f.read()) #！此时f指向末尾空的位置，所以输出的是一个空行
f.close()