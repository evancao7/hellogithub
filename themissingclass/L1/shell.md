~ 表示当前位于 home 目录下。
$ 符号表示您现在的身份不是 root 用户。
使用 pwd 命令可以查看当前的工作目录。
cd (change directory）命令来切换目录。其中 .. 表示退回到上级目录。
撤销目录切换。当切换到其他目录后如果想回退到切换前的目录中，可以采用 cd - 来实现,返回到上一步所在目录
ls 命令用于查看当前目录下的文件。

如果您希望传递的参数中包含空格（例如一个名为 My Photos 的文件夹），您要么用使用单引号，双引号将其包裹起来，要么使用转义符号 \ 进行处理（My\ Photos）。

ls -l 可以更详细的打印文件或文件信息。
Evans-MacBook-Pro:python Evan$ ls -l
total 48
drwxr-xr-x   4 Evan  staff   128  1  1 11:03 day3
drwxr-xr-x  11 Evan  staff   352  1  6 11:20 day4
-rw-r--r--   1 Evan  staff   599 12 31 17:19 for_loop.py
-rw-r--r--   1 Evan  staff  1689 12 31 18:49 hello.py
-rw-r--r--   1 Evan  staff     6  1  8 14:37 shell.txt
-rw-r--r--   1 Evan  staff    10  1  8 14:41 shell2.txt
-rw-r--r--   1 Evan  staff   811  1  6 10:45 str.py
-rw-r--r--   1 Evan  staff   218 12 31 17:21 选车牌.py
Evans-MacBook-Pro:python Evan$ ls -l | tail -n1
-rw-r--r--   1 Evan  staff   218 12 31 17:21 选车牌.py
Evans-MacBook-Pro:python Evan$ 

r (read) 代表可读。
w (write) 代表可写也就是具有修改权。
x 代表可执行。
- 则代表该用户不具备相应的权限。

其中 tail 命令表示从尾部开始查看文件，参数 n 后面的数字表示具体要查看几行。

也可以将信息输出流 (>) 写入文本中。shell.txt的地址是当前文件夹下
|的作用，将左边的内容作为输入，写入右边，如下面句子，功能是将ls -l的结果作为输入给tail，而tail的功能是将输入内容的最后一行开始选一行输出，这里-n1代表选择最后一行
Evans-MacBook-Pro:python Evan$ ls -l | tail -n1 > shell.txt 
Evans-MacBook-Pro:python Evan$ cat shell.txt 
-rw-r--r--   1 Evan  staff   218 12 31 17:21 选车牌.py
Evans-MacBook-Pro:python Evan$ 

如果你要求 shell 执行某个指令，但是该指令并不是 shell 所了解的编程关键字，那么它会去咨询 环境变量 $PATH，它会列出当 shell 接到某条指令时，进行程序搜索的路径：结果是包含多个个地址的list，程序要运行时会去各个地址找
Evans-MacBook-Pro:~ Evan$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/aria2/bin:/Library/Apple/usr/bin:/Users/Evan/maven/apache-maven-3.6.3/bin

which 命令 语句，返回在哪个文件夹找到这个命令
Evans-MacBook-Pro:L1 Evan$ which echo
/bin/echo
Evans-MacBook-Pro:L1 Evan$ which man
/usr/bin/man

如果忘记命令的相关内容，可以使用 man 来查看该命令的用户手册。
例如 man ls ,注意按 q 可以退出查看界面。
man 可以获得比 help 更多的信息。


信息的流动称为流，程序中存在两个流。
流入程序的称为输入流，流出的则称为输出流。
程序读取信息时会从输入流中进行读取，相反打印信息时则是输出到输出流中。
例如重定向 > 可以将程序的输入流和输出流分别重定向到文件中。
最简单的重定向是 < file 和 > file。这两个命令可以将程序的输入输出流分别重定向到文件：
Evans-MacBook-Pro:python Evan$ ls
day3		day4		for_loop.py	hello.py	shell.txt	str.py		选车牌.py

Evans-MacBook-Pro:python Evan$ echo 0>shell2.txt 

cat输出文件的内容
Evans-MacBook-Pro:python Evan$ cat shell
shell.txt   shell2.txt  
Evans-MacBook-Pro:python Evan$ cat shell2.txt 
Evans-MacBook-Pro:python Evan$ cat shell.txt 
shell
将shell里的内容写到shell2里面，相当于cp
Evans-MacBook-Pro:python Evan$ cat <shell.txt > shell2.txt 
Evans-MacBook-Pro:python Evan$ cat shell2.txt 
shell
Evans-MacBook-Pro:python Evan$ 

>> 表示追加内容
Evans-MacBook-Pro:python Evan$ echo ppp >> shell2.txt 
Evans-MacBook-Pro:python Evan$ cat shell2.txt 
shell
ppp
Evans-MacBook-Pro:python Evan$ 


根用户在类 Unix 系统中是非常强大的，拥有整个系统的所有权限。
通过 su (super user 缩写) 命令进行切换到根用户，也称为超级用户或 root 用户。
因为根用户权限比较高， 所以通常不建议处于根用户的状态避免误操作。 但是执行某些命令是权限不够，sudo 命令用于解决这个问题，也就是可以以 su 的身份来 do 一些事情。
需要填写密码，#表示管理员的身份了，通过exit退出
vans-MacBook-Pro:~ Evan$ sudo su
Password:
sh-3.2# 
sh-3.2# exit

mv,将文件夹missing移到L1中
Evans-MacBook-Pro:themissingclass Evan$ mv missing L1
mv，将文件名为semeter改为highschool
Evans-MacBook-Pro:L1 Evan$ mv semester highschool

cp，将shell.txt的内容复制到shell2.txt中
Evans-MacBook-Pro:L1 Evan$ cp shell.txt shell2.txt 
cp，将shell.txt的内容复制到shell3.txt中,如果shell3.txt本身不存在就先新建然后写入
Evans-MacBook-Pro:L1 Evan$ cp shell.txt  shell3.txt

rm  移除文件，不能移除文件夹
Evans-MacBook-Pro:L1 Evan$ rm shell3.txt 

rmdir 移除文件夹，只有文件夹为空时才能执行
Evans-MacBook-Pro:themissingclass Evan$ rmdir L1
rmdir: L1: Directory not empty

mkdir 创建
Evans-MacBook-Pro:themissingclass Evan$ mkdir 'L3'

touch语句
Evans-MacBook-Pro:L1 Evan$ touch semester

./文件名表示执行文件
Evans-MacBook-Pro:L1 Evan$ ./semester
-bash: ./semester: Permission denied
查看如何更改模式
Evans-MacBook-Pro:L1 Evan$ man chmod
查看文件现在的权限
Evans-MacBook-Pro:L1 Evan$ ls -l semester 
-rw-r--r--@ 1 Evan  staff  61  1  8 17:23 semester
权限改为可编辑
Evans-MacBook-Pro:L1 Evan$ chmod +x semester 
Evans-MacBook-Pro:L1 Evan$ ls -l semester 
-rwxr-xr-x@ 1 Evan  staff  61  1  8 17:23 semester
运行文件
Evans-MacBook-Pro:L1 Evan$ ./semester 
Evans-MacBook-Pro:L1 Evan$ ls -l last-modified.txt 
-rw-r--r--@ 1 Evan  staff  0  1  8 17:33 last-modified.txt
777将权限全部开放
Evans-MacBook-Pro:L1 Evan$ chmod 777 last-modified.txt 
Evans-MacBook-Pro:L1 Evan$ ls -l last-modified.txt 
-rwxrwxrwx@ 1 Evan  staff  0  1  8 17:33 last-modified.txt

#!/bin/sh
有用，这些不是注释符，而是说明下面的脚本是在什么shell下面运行的，并且以该shell环境来执行脚本