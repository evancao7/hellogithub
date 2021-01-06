#类似结构体和无序map，用的是大括号
dic={}
dic[1]=1
dic['2']=2
print(dic)
dic[1]=4      #key键值唯一，所以会覆盖之前键值为1对应的value
print(dic)
#同理通过d.pop()删掉并返回 和 del d[1]进行删除
print(1 in dic)   #d中是否有以1作为键值的元素，返回布尔值
print(dic.keys())   #返回dic中所有的键值
print( dic.items()) #将每对key，value组成一个list
for k in dic:
    print(k,dic[k])     #取出k和dic[k]
print(len(dic))     #求dic的长度
dic["a"]={"salary":5000,"age":28}   #dic的嵌套
print(dic)
print(dic["a"]["age"])      #对嵌套的读取