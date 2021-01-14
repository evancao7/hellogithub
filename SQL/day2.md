USE myemployees;
 要先选中命令再执行
`通过来区分字段和关键字`

desc 表名; 查看指定表的结构

#1.查询表中的单个字段
SELECT last_name FROM employees;

#2.查询表中多个字段
SELECT last_name,salary,email FROM employees;

#3.查询表中的所有字段
SELECT * FROM employees;

#4.查询常量
# select 常量值;
# 注意：字符型和日期型的常量值必须用单引号引起来，数值型不需要
SELECT 100;
SELECT 'join';

#5.查询函数
#select 函数名(实参列表);
SELECT VERSION();

#6.查询表达式 
SELECT 100%98;

#7.起别名
/*
1.便于理解
2.如果要查询的字段有重名的情况,使用别名区分
*/
#方式一:使用AS
SELECT 100%98 AS 结果;
SELECT last_name AS 姓,first_name AS 名 FROM employees;

#方式二:使用空格
SELECT last_name 姓,first_name 名 FROM employees;

#案例:查询salary,结果显示 out put
SELECT salary AS "out put" FROM employees;

#8.去重
# select distinct 字段名 from 表名;
#案例:查询员工表中涉及的所有部门编号
SELECT DISTINCT department_id FROM employees;

#9.+号的作用
#案例:查询员工的名和姓,并显示为姓名
/*
java中的+号:
1.运算符:两个操作数都为数据型
2.连接符:只要有一个操作数为字符串


mysql中的+号:
只能作为运算符

select 100+90; 两个操作数都为数值型,做加法运算
select '123+90';其中一方为字符型,试图将字符型数值转换为数值型
		如果转换成功,则继续做加法运算
select 'john'+90; 如果转换失败,则将字符型数值转换成0

!!
select null+0; 只要其中一方为null,则结果肯定为null.
*/
SELECT last_name+first_name AS 姓名 FROM employees; 

#10.【补充】concat函数 
/*
功能：拼接字符
select concat(字符1，字符2，字符3,...);
*/
SELECT CONCAT('a','b','c') AS 结果 FROM employees;

SELECT CONCAT(last_name,first_name) AS 姓名 FROM employees;

#11.【补充】ifnull函数
#功能：判断某字段或表达式是否为null，如果为null 返回指定的值，否则返回原本的值

SELECT IFNULL(commission_pct,0) FROM employees;

#12.【补充】isnull函数
#功能：判断某字段或表达式是否为null，如果是，则返回1，否则返回0
