#-*- coding:utf-8 -*-

#打开文件的open函数
f = open("./C++test.cpp")
line = f.readline()#readline()读取文件的每一行
if (line):
	print("The file has opend!")

#用while和for循环的区别：while会将文件的每一行都读取出来，for则会跳过第一行
#原因：while是循环，每一行都进行循环判断，而for是迭代，

#while loop
#while line:
#	print(line, end = '')
#	line = f.readline()

ofile = open("./C++test.cpp","w")

#for loop
for line in f:
#	print(line, end = '')
#	print(line, end = '', file = ofile)
	ofile.write(line)
ofile.close()
f.close()
