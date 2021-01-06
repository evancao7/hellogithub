a=['p','q','r']
b=['2','3','5']
a.extend(b)     #b接到a的后面
print(a)
a.insert(2,['er','po'])
print(a)
print(a[2][1])  #取出po
print(a.pop())  #删除list最后一个元素
print(a)
print(a.pop(-2))    #！！从右往左数的时候是-1,-2这样的数，从左往右是1，2，3，在取值时也可这样进行
print(a[-1])
a.clear     #清空
print(a[0:3])   #链表切片
print(a[:3])    #省略0是简写的方式
print(a[3:])    #取下标3及之后的所有值,也是省略写法
print(a[-2:])   #倒切的情况，从下标-2取到-1，不能-2:-1，因为这样就取不到-1了
a[1: :2]    #从下标1开始隔1个取1个
print(a)
del a[2]    #当a中既有list又有str时，无法排序，所以要删掉一种，只剩相同的类型
a.sort()
print(a)
a.reverse() #反转
print(a)
for i in a:     #循环输出a中的元素
    print(i)
    