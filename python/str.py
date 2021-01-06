a="hello i am evan"
print(a[1:3])   #下标1到3的元素，左闭右开
#a[2]="p" 会报错，因为a[2]赋值之后 不能再被更改，字符串和数字为不可变类型
print(a.count('l'))     #a中l出现的次数，'l'  "l"都可
print(a.count('l',0,3))     #从下标0～下标3，左闭
print(a.endswith("lo"))     #返回True或False
print(a.startswith('j'))    #同理
a.find('w')     #返回布尔值
a.isdigit( )    #是否为数字
print('22'.isdigit( ))  #一定要加引号
print(a.replace('l','p',1))   #默认全部替换，后面加上数字表示替换几个，顺序从左到右,注意字符串是不能被更改到，所以要有一个字符串变量来接收，这里是直接输出了新的字符串变量
print(a.split())    #可以实现一些更细节的划分,默认按空格区分