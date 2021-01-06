f=open("联系表.txt","r")
for line in f:
    print(line,end="")  #防止文件本身每行自带的换行符
print()

f=open("联系表.txt","r")
for line in f:
    line=line.split()   #将行的元素以空格为分割形成链表
    height=int(line[1]) #链表中的元素默认为字符串，这里将字符串强转为int
    age=int(line[2])
    if height<180 and age<40:
        print(line)     #输出链表