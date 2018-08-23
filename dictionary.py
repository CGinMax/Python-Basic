#-*- coding:utf-8 -*-
a_dic = {"CGinMax":20, "Hao":21, "sen":22}
print(str(a_dic))
#获取键所对应的值
print("My age: " + str(a_dic["CGinMax"]))

#添加键值
a_dic["Hao"] = 21
print("Hao truly age :" + str(a_dic["Hao"]))

a_dic["Elliot"] = 40
print("Add Elliot" + str(a_dic))

#删除
del a_dic["sen"]
print("After del:" + str(a_dic))

#a_dic.clear()
#print("After clear" + str(a_dic))

#比较两个字典的方法
mul_dic = {"my":412, "Hao":434, "liang":442}
#print("Compare two dictionary:" + cmp(a_dic, mul_dic))

#计算元素个素
the_len = len(mul_dic)
print("mul_dic length is: " + str(the_len))

#返回一个字典的浅拷贝
copy_dic = mul_dic.copy()
print("The copy_dic is " + str(copy_dic))
del copy_dic

#创建新字典
new_dic = mul_dic.fromkeys(("Me", "Mother", "Brother"), (1, 2, 3))
print("The new dictionary is " + str(new_dic))

#get函数,如果键不存在，返回None的值
print("Hao CET-4:" + str(mul_dic.get("Hao", None)))

#setdefault，为旧键设新值，为新建添加默认值
a_dic.setdefault("Happy", 25)
print("After setdefault :" + str(a_dic))

#把mul_dic的值更新到a_dic
a_dic.update(mul_dic)
print("a_dic change to " + str(a_dic))

#items
print("After items" + str(mul_dic.items()))

#以列表的方式返回所有键
print("mul_dic key list :" + str(mul_dic.keys()))

#以列表方式，返回字典中所有的值
print("Dictionary value list" + str(mul_dic.values()))
