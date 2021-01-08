注意不能使用空格分割，bash 会以空格为单位进行解释。 如果以空格进行分割，例如： foo = bar bash 会将调用 foo 程序将 = 和 bar 作为参数。
访问变量 $foo
Evans-MacBook-Pro:L1 Evan$ foo=bar
Evans-MacBook-Pro:L1 Evan$ echo $foo
bar
Evans-MacBook-Pro:L1 Evan$ echo '$foo'
$foo
Evans-MacBook-Pro:L1 Evan$ echo "$foo"
bar
Evans-Ma

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
进入vim后按i进入insert，按esc+：+wq+回车退出,实现保存然后退出

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