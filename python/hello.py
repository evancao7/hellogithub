
#字符串用" " , ' '单双引号都可以，只要前后对应即可，多引号可用于跨行的变量定义
name1="evan"
#调用时直接写变量名，id()取货物所在的内存地址
#变量名第一个不能是数字，驼峰体（首字母大写），或下划线
AgeOfOldboy=67
age_of_oldboy=77
print(name1,id(name1))

#修改变量
name1="Kai"
print(name1)
#删除变量
#del name1

#这里指向同一个货物，所以地址一致
name2= name1
print(id(name1),id(name2))
#改变name1，name2不改变,因为name2指向的是Kai，而不是name1，指向不同货物之后，地址不一样
name1="PPP"
print(name1,name2)
print(id(name1),id(name2))

#输出变量类型
print(type(name1))

#列表，类比数组
names=['ab','ds','fj','ig']
print(names[3])
names.insert(3,'hhh')
#下标为3处增加了hhh
print(names[3])
#删除，也可以用remove
del names[3]
print(names[3])

#10**20，10的20次幂；9//2结果为4，整除，取整数
#比较运算，与c一致
#逻辑运算 and等价于&& or等价于｜｜ not等价于！  a>0 or b<5 and c<10等价于 a>0 or (b<5 and c<10),即or后面为一个整体
#成员运算 in 和 not in用来测试字符串、列表、元祖、字典、集合，但是不能用于数字

#开发工具选中后command+? 整体注释

#读入信息到username中,input读的值都是字符串，所以要强制转化为数字n1=int(nput("your name:")),相应的数字转字符串为str()
username=input("your name:")
print(username)

#格式化输出,f,{ 变量名 }
print(f"my name is {username}")

salary=8000
if salary<10000:
    #通过缩进实现包含关系，tab相当于四个空格，if elif else
    print(f"{salary} too less")