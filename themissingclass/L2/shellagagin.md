注意不能使用空格分割，bash 会以空格为单位进行解释。 如果以空格进行分割，例如： foo = bar bash 会将调用 foo 程序将 = 和 bar 作为参数。
访问变量 $foo
Evans-MacBook-Pro:L1 Evan$ foo=bar
Evans-MacBook-Pro:L1 Evan$ echo $foo
bar
Evans-MacBook-Pro:L1 Evan$ echo '$foo'
$foo
Evans-MacBook-Pro:L1 Evan$ echo "$foo"
bar


单引号和双引号不同，单引号内部的内容会原样输出。双引号则会进行相应的替换
Evans-MacBook-Pro:L1 Evan$ echo "value of foo is $foo"
value of foo is bar
Evans-MacBook-Pro:L1 Evan$ echo 'value of foo is $foo'
value of foo is $foo


这里 $1 是脚本的第一个参数。与其他脚本语言不同的是，bash使用了很多特殊的变量来表示参数、错误代码和相关变量。下面是列举来其中一些变量，
$0 - 脚本名
$1 到 $9 - 脚本的参数。 $1 是第一个参数，依此类推。
$@ - 所有参数
$# - 参数个数
$? - 前一个命令的返回值
$$ - 当前脚本的进程识别码
!! - 完整的上一条命令，包括参数。常见应用：当你因为权限不足执行命令失败时，可以使用 sudo !!再尝试一次。
$_ - 上一条命令的最后一个参数。如果你正在使用的是交互式shell，你可以通过按下 Esc 之后键入 . 来获取这个值。
进入vim后按i进入insert，按esc+：+wq+回车退出,实现保存然后退出 :+q实现不保存退出

用vim创建并编辑sh文件
Evans-MacBook-Pro:L2 Evan$ vim mcd.sh
    文件内容
    mcd () {
    mkdir -p "$1"
    cd "$1"
    }
Evans-MacBook-Pro:L2 Evan$ ls
mcd.sh		shellagagin.md
增加mcd作为一个新命令行
Evans-MacBook-Pro:L2 Evan$ source mcd.sh
执行mcd命令，效果就是创建一个名为 test的文件，并且进入，这里就是对mcd的理解
Evans-MacBook-Pro:L2 Evan$ mcd test
Evans-MacBook-Pro:test Evan$ 

grep A B 在B中寻找A，如果含有其内容的行，返回值为0；如果没有返回值为1
Evans-MacBook-Pro:L2 Evan$ grep foobar mcd.sh 
Evans-MacBook-Pro:L2 Evan$ $?
因为mcd中没有foobar所以grep这条指令返回的值是1
-bash: 1: command not found
Evans-MacBook-Pro:L2 Evan$ grep '$1' mcd.sh 
 返回含有内容的行
 mkdir -p "$1"
 cd "$1"
Evans-MacBook-Pro:L2 Evan$ $?
-bash: 0: command not found
Evans-MacBook-Pro:L2 Evan$ echo 'hello'
hello
Evans-MacBook-Pro:L2 Evan$ $?
因为上一个echo语句正常执行了，所以返回值为0
-bash: 0: command not found


退出码可以搭配&& (与操作符) 和 || (或操作符)使用，用来进行条件判断，决定是否执行其他程序。同一行的多个命令可以用 ; 分隔。程序 true 的返回码永远是0，false 的返回码永远是1。
先执行false，发现不行，再执行echo，发现可以
false || echo "Oops, fail"
# Oops, fail

先执行true，发现可以，就不再执行echo了
true || echo "Will not be printed"
#

如果第一部分是true才会执行第二部分
true && echo "Things went well"
# Things went well

如果第一部分就是false，就不会执行第二部分了
false && echo "Will not be printed"
#

；用于分隔两个命令
false ; echo "This will always run"
# This will always run


当您通过 $( CMD ) 这样的方式来执行CMD 这个命令时，然后它的输出结果会替换掉 $( CMD ) 。例如，如果执行 for file in $(ls) ，shell首先将调用ls ，然后遍历得到的这些返回值。还有一个冷门的类似特性是 进程替换（process substitution）， <( CMD ) 会执行 CMD 并将结果输出到一个临时文件中，并将 <( CMD ) 替换成临时文件名。这在我们希望返回值通过文件而不是STDIN传递时很有用。例如， diff <(ls foo) <(ls bar) 会显示文件夹 foo 和 bar 中文件的区别。
将pwd返回的内容赋值给foo
Evans-MacBook-Pro:~ Evan$ foo=$(pwd)
输出变量时前面要加$d代表这是一个变量
Evans-MacBook-Pro:~ Evan$ echo "$foo"
/Users/Evan

注意要加括号的
Evans-MacBook-Pro:~ Evan$ echo "now is $(date)"
now is 2021年 1月 9日 週六 09時41分56秒 CST

打开当前所在文件夹
Evans-MacBook-Pro:L2 Evan$ open $(pwd)

Evans-MacBook-Pro:L2 Evan$ vim example.sh
    #!/bin/bash

    echo "Starting program at $(date)" # date会被替换成日期和时间

    echo "Running program $0 with $# arguments with pid $$"

    for file in $@; do
        grep foobar $file > /dev/null 2> /dev/null
        # 如果模式没有找到，则grep退出状态为 1
        # 我们将标准输出流和标准错误流重定向到Null，因为我们并不关心这些信息
        if [[ $? -ne 0 ]]; then     -ne表示如果不相等,等价于[$? !=0]
            echo "File $file does not have any foobar, adding one"
            echo "# foobar" >> "$file"
        fi
    done

获得权限后用example脚本执行自身，因为自身含有foobar字符串，所以if语句不满足
Evans-MacBook-Pro:L2 Evan$ ./example.sh  example.sh 
Starting program at 2021年 1月 9日 週六 10時07分00秒 CST
Running program ./example.sh with 1 arguments with pid 34855

用example执行mcd，因为mcd中不含foobar，所以if语句要执行
Evans-MacBook-Pro:L2 Evan$ ./example.sh mcd.sh 
Starting program at 2021年 1月 9日 週六 10時09分57秒 CST
Running program ./example.sh with 1 arguments with pid 34928
File mcd.sh does not have any foobar, adding one

新建了一个只含字符串aaa的文件try1.sh，这里一次运行两个文件，所以变量为2
Evans-MacBook-Pro:L2 Evan$ ./example.sh example.sh try1.sh 
Starting program at 2021年 1月 9日 週六 10時12分49秒 CST
变量数量为2
Running program ./example.sh with 2 arguments with pid 35025
File try1.sh does not have any foobar, adding one

找到当前路径中所有以.sh结尾的文件
Evans-MacBook-Pro:L2 Evan$ ls *.sh
example.sh	mcd.sh		try1.sh

当执行脚本时，我们经常需要提供形式类似的参数。bash使我们可以轻松的实现这一操作，它可以基于文件扩展名展开表达式。这一技术被称为shell的 通配（ globbing）
通配符 - 当你想要利用通配符进行匹配时，你可以分别使用 ? 和 * 来匹配一个或任意个字符。 注意？只能代替一个字符，？能代表任意多个字符
Evans-MacBook-Pro:L2 Evan$ touch p1 p2 p3 p4
Evans-MacBook-Pro:L2 Evan$ ls
example.sh	p1		p3		shellagagin.md	try1.sh
mcd.sh		p2		p4		test		try2.sh
Evans-MacBook-Pro:L2 Evan$ ls p?
p1	p2	p3	p4
Evans-MacBook-Pro:L2 Evan$ touch p44
？只能代表一个字符
Evans-MacBook-Pro:L2 Evan$ ls p?
p1	p2	p3	p4
*能代替任意多个字符
Evans-MacBook-Pro:L2 Evan$ ls p*
p1	p2	p3	p4	p44


花括号{} - 当你有一系列的指令，其中包含一段公共子串时，可以用花括号来自动展开这些命令。这在批量移动或转换文件时非常方便。
Evans-MacBook-Pro:L2 Evan$ ls
1.gif		mcd.sh		p2		p4		shellagagin.md	try1.sh
example.sh	p1		p3		p44		test		try2.sh
Evans-MacBook-Pro:L2 Evan$ touch foo{,1,2,10}  效果相当于touch foo foo1 foo2 foo10
Evans-MacBook-Pro:L2 Evan$ ls
1.gif		foo1		mcd.sh		p3		shellagagin.md	try2.sh
example.sh	foo10		p1		p4		test
foo		foo2		p2		p44		try1.sh
移除foo文件
Evans-MacBook-Pro:L2 Evan$ rm foo{,1,2,10}
Evans-MacBook-Pro:L2 Evan$ ls
1.gif		mcd.sh		p2		p4		shellagagin.md	try1.sh
example.sh	p1		p3		p44		test		try2.sh
Evans-MacBook-Pro:L2 Evan$ 

注意，脚本并不一定只有用bash写才能在终端里调用。比如说，这是一段Python脚本，作用是将输入的参数倒序输出：
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
shell知道去用python解释器而不是shell命令来运行这段脚本，是因为脚本的开头第一行的shebang。它指明了执行这个脚本文件的解释程序。

Evans-MacBook-Pro:L2 Evan$ python3 script.py a b c
c
b
a

Evans-MacBook-Pro:L2 Evan$ ./script.py a b c
-bash: ./script.py: Permission denied
Evans-MacBook-Pro:L2 Evan$ chmod 777 script.py 
Evans-MacBook-Pro:L2 Evan$ ./script.py a b c
c
b
a

当我把shebang改成#!/usr/bin/ 后，由于没有指定解释器，所以会出现如下错误
Evans-MacBook-Pro:L2 Evan$ ./script.py a b c
-bash: ./script.py: /usr/bin/: bad interpreter: Permission denied
但是如果我直接用命令行python3执行，也就是告诉电脑我要用python3解释器来解释这个文件，所以就不会出现上面的错误
Evans-MacBook-Pro:L2 Evan$ python3 script.py a b c
c
b
a


将shebang改为 #!/usr/bin/env python3 功能就是去环境里找python3的地址，告诉程序用python3的解释器来解释
这样以来，也能直接执行
Evans-MacBook-Pro:L2 Evan$ ./script.py a b c
c
b
a

编写 bash 脚本有时候会很别扭和反直觉。例如 shellcheck这样的工具可以帮助你定位sh/bash脚本中的错误。
Evans-MacBook-Pro:L2 Evan$ shellcheck mcd.sh 
这里就提示说没有写shebang
In mcd.sh line 1:
mcd () {
^-- SC2148: Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive.

通过brew安装新的命令行 tldr 是too long didin't read的简写，比man好用多了
Evans-MacBook-Pro:L2 Evan$ tldr mv

mv

Move or rename files and directories.

- Move files in arbitrary locations:
    mv source target

- Do not prompt for confirmation before overwriting existing files:
    mv -f source target

- Prompt for confirmation before overwriting existing files, regardless of file permissions:
    mv -i source target

- Do not overwrite existing files at the target:
    mv -n source target

- Move files in verbose mode, showing files after they are moved:
    mv -v source target

# 查找所有名称为src的文件夹,这里的.代表在当前文件夹里寻找
find . -name src -type d
# 查找所有文件夹路径中包含test的python文件
find . -path '**/test/**/*.py' -type f
# 查找前一天修改的所有文件
find . -mtime -1
# 查找所有大小在500k至10M的tar.gz文件
find . -size +500k -size -10M -name '*.tar.gz'

find有很多不同的用法，通过tldr来查询，这里是找当当前路径下在1天内更改过的文件
Evans-MacBook-Pro:L2 Evan$ find . -mtime -1
.
./.DS_Store
./target.tar.gz
./target
./try2.sh
./shellagagin.md
./try1.sh
./script.py

find在找到文件之后还能对文件进行操作，这里是将文件名为p开头对rm删除掉
Evans-MacBook-Pro:target Evan$ find . -name 'p*' -exec rm {} \;

大多数人都认为 find 和 fd 已经很好用了，但是有的人可能想知道，我们是不是可以有更高效的方法，例如不要每次都搜索文件而是通过编译索引或建立数据库的方式来实现更加快速地搜索。
fd语句
Evans-MacBook-Pro:L2 Evan$ fd '^p'
p1
p2
p3
p4
p44

没有具体使用，跳过了
这就要靠 locate 了。 locate 使用一个由 updatedb负责更新的数据库，在大多数系统中 updatedb 都会通过 cron每日更新。这便需要我们在速度和时效性之间作出权衡。而且，find 和类似的工具可以通过别的属性比如文件大小、修改时间或是权限来查找文件，locate则只能通过文件名。 here有一个更详细的对比。

命令行最后对 .不能漏掉
Evans-MacBook-Pro:L2 Evan$ grep -R foobar .
./example.sh:    grep foobar $file > /dev/null 2> /dev/null
./example.sh:        echo "File $file does not have any foobar, adding one"
./example.sh:        echo "# foobar" >> "$file"
./try2.sh:# foobar
./mcd.sh:# foobar
./shellagagin.md:Evans-MacBook-Pro:L2 Evan$ grep foobar mcd.sh 
./shellagagin.md:因为mcd中没有foobar所以grep这条指令返回的值是1
./shellagagin.md:        grep foobar $file > /dev/null 2> /dev/null
./shellagagin.md:            echo "File $file does not have any foobar, adding one"
./shellagagin.md:            echo "# foobar" >> "$file"
./shellagagin.md:获得权限后用example脚本执行自身，因为自身含有foobar字符串，所以if语句不满足
./shellagagin.md:用example执行mcd，因为mcd中不含foobar，所以if语句要执行
./shellagagin.md:File mcd.sh does not have any foobar, adding one
./shellagagin.md:File try1.sh does not have any foobar, adding one
./try1.sh:# foobar


与 find/fd 一样，重要的是你要知道有些问题使用合适的工具就会迎刃而解，而具体选择哪个工具则不是那么重要。
rg命令
# 查找所有使用了 requests 库的文件
rg -t py 'import requests'
# 查找所有没有写 shebang 的文件（包含隐藏文件）
rg -u --files-without-match "^#!"
# 查找所有的foo字符串，并打印其之后的5行
rg foo -A 5
# 打印匹配的统计信息（匹配的行和文件的数量）
rg --stats PATTERN

查找shell命令
history 命令允许您以程序员的方式来访问shell中输入的历史命令。这个命令会在标准输出中打印shell中的里面命令。如果我们要搜索历史记录，则可以利用管道将输出结果传递给 grep 进行模式搜索。 history | grep find 会打印包含find子串的命令。

fish的好处,在fish中不支持$(pwd),反之用(pwd)代替
另外一个和历史命令相关的技巧我喜欢称之为基于历史的自动补全。 这一特性最初是由 fish shell 创建的，它可以根据您最近使用过的开头相同的命令，动态地对当前对shell命令进行补全。这一功能在 zsh 中也可以使用，它可以极大的提高用户体验。
在fish模式下，
Evans-MacBook-Pro:L2 Evan$ 我改成了Evan Says : 这样的坏处就是说不能直观看到自己所处的文件夹和权限，可以通过exit命令退出
Evan Says : tree
.
├── 1.gif
├── example.sh
├── mcd.sh
├── p1
├── p2
├── p3
├── p4
├── p44
├── script.py
├── shellagagin.md
├── target
├── target.tar.gz
├── test
├── try1.sh
└── try2.sh

2 directories, 13 files

broot能通过输入来快速匹配相应的文件

xargs命令的作用，是将标准输入转为命令行参数
https://www.ruanyifeng.com/blog/2019/08/xargs-tutorial.html
由于xargs默认将空格作为分隔符，所以不太适合处理文件名，因为文件名可能包含空格。

find命令有一个特别的参数-print0，指定输出的文件列表以null分隔。然后，xargs命令的-0参数表示用null当作分隔符。
将左边找到的文件作为参数赋给zip命令，对每一个文件执行一次zip命令
Evans-MacBook-Pro:L2 Evan$ find . -name '*.sh' -print0 | xargs -0 zip out.zip 
  adding: example.sh (deflated 24%)
  adding: try2.sh (stored 0%)
  adding: macro.sh (deflated 24%)
  adding: mcd.sh (deflated 7%)
  adding: try1.sh (deflated 6%)

没太理解
(进阶) 编写一个命令或脚本递归的查找文件夹中最近使用的文件。更通用的做法，你可以按照最近的使用时间列出文件吗？
  fd . -0 -t f | xargs -0 stat -f '%m%t%Sm %N' | sort -n | cut -f2- | tail -n 1

在项目级别下标记自己的标签，目的就是告知这一部分是谁提交的，相应的就有系统级别的标签，这里没有写了
~/D/g/h/t/L2 ❯❯❯ git config user.name evan_L2
~/D/g/h/t/L2 ❯❯❯ git config user.email evanckj@gmail.com
~/D/g/h/t/L2 ❯❯❯ cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[user]
	name = evan_L2
	email = evanckj@gmail.com