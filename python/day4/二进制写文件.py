f=open("自己写内容进去","wb")
s='路飞'
s=s.encode("gbk")   #以gbk模式读入，一定要以gbk显示才行，如果用utf-8就是乱码
f.write(s)
f.write("路飞") #就会报错，因为只能输入二进制文件，这里路飞是字符串