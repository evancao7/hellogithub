black_girl_age=26
for i in range(3):
   guess=(int(input("your guess:")))
   if guess>black_girl_age:
       print("太大了")
   elif guess<black_girl_age:
       print("猜小了")
   else:#exit()打印猜对了，并退出
       exit("猜对了")
   if i==2:
        print("用完了")

for i in range(1,3)#i取值范围是1、2

#while
count=0
while count<=10:
    print(count)
    count+=1

#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        #print自动换行，这里end=" "表示不换行，改成添加一个空格
        print(f"{i}X{j}={i*j}",end=" ")
    print( )

