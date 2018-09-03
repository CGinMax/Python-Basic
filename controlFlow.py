# -*- coding:utf-8 -*-

age = 18
m_age = int(input("Say you age: "))

if m_age == age:
	print("You age just safing")
elif m_age < age:
	print("You are yongest")
elif m_age > age:
	print("Welcome")
else:
	print("Error")

#for
#range(num1,num2),从num1迭代到num2.[num1,num2)，半开区间
for i in range(0, m_age):
	print(i, end = " ")
print("Done")

#for遍历列表
a_list = [0, 4, 8, 7, 1, 2]
print("遍历列表")
for i in a_list:
	print(i, end = ",")
print()

#for遍历元组
a_tuple = (3, 2, 5, 7, 6, 1)
print("遍历元组")
for i in a_tuple:
	print(i, end = "," )
print()

#for遍历字典
a_dic = {"CGinMax":"42", "Elliot":"23", "Hao":"37", "Xian":"1"}
print("遍历字典")
for ele in a_dic:
	print(ele)
	print(a_dic[ele])

#字典根，键 同时迭代
for key, elem in a_dic.items():
	print(key, elem)

#while用于循环
while m_age != age:
	m_age = int(input("Enter you age again: "))
	if m_age < 0:
		print("Program is break")
		break
	if m_age == age:
		print("Oh!You are right here")
	else:
		print("No!You need to try it again")

#pass,退出本次判断，继续执行下面的程序
print("Using pass")
for iter1 in a_list:
	if not iter1:
#		continue
		pass
	print("The iter1 is " + str(iter1))
