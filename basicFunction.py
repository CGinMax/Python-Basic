# -*- coding:utf-8 -*-
#无返回值
def print_my_name():
	print("CGinMax")

print_my_name()

def print_pep_name(name):
	print(str(name))
print_pep_name("Elliot")

#有返回值
def binary_value(value, time):
	finally_value = value * time
	return finally_value

my_value = binary_value("1010", 4)
print("My value is " +  my_value)

#全局变量和局部变量
x = 3
def local_change(x):
	print("x is " + str(x))
	x = 12
	print("x was changed to " + str(x))

local_change(x)
print("local_change the number of X " + str(x))
del x

y = 10
def global_change():
        print("y is " + str(y))
        global y
        y = 20
        print("After change y is " + str(y))
global_change()
print("global_change the number of y " + str(y))
del y

#关键字参数
def key_word(a = 4, b = 5, c = 6):
	print("a is ", a, "b is ", b, "c is ", c)

key_word()
key_word(a = 10, c = 72)
key_word(b = 8, c = 31)
key_word(c = 10, b = 20, a = 30)

#Var args参数
#一个*:表示多个参数以元组的形式传入，多个*:表示已命名的变量以字典的方式传入
def print_paras(para, *nums, **words):
	print("para :" + str(para))
	print("nums :" + str(nums))
	print("words :" + str(words))

print_paras("CGinMax", 2, 4, 5, 6, name = "Elliot", he_name = "Hao")


