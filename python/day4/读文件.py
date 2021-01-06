f=open("list","r")  #r处如果不写就是默认为r即等价于 f=open("list")
print(f.readline()) #输出光标所指的第一行，因为这里的f是刚获得的，所以第一行就是文件的第一行，print本身会换行，然后readline又会换行所以会空一行
print("--------")   #作为分割
print(f.read())     #此时光标在第二行，所以虽然是f.read( )但实际是从光标所指处开始，读到最末尾，即第一行在此不输出