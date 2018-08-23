#*-* coding-utf8 *-*

a_list = [1]
mul_list = [1, 4, 7, ['r', 'l', 'n']]
print(mul_list)
print(mul_list[3][2])

#列表基本函数
#cmp(a_list, mul_list)#比较两个列表的元素，返回
print("列表长度：", len(mul_list))
#max(mul_list)
#不能用与int元素和list元素进行比较
#min(mul_list)

#列表元素操作函数
a_list.append(11)
print("a_list.append:", a_list)

print("a_list.count:", a_list.count(1))#列出元素在列表出现的次数

a_list.extend(mul_list)#在列表末尾加上另一个列表
print("a_list.extend:", a_list)

print("mul_list[4] index:", mul_list.index(4))#查找元素在列表中的索引

a_list.insert(2, 't')
print("a_list.insert:", a_list)

mul_list.pop()#pop直接将列表里的列表整个弹出
print("mul_list.pop:", mul_list)

print("a_list.remove: ", a_list.remove(4))

#列表的元素全部翻转
a_list.reverse()
print("a_list.reverse: ", a_list)


print("将列表转为元组:", tuple(mul_list))


print("-----------------------------")

a_tuple = (2,)
#print(type(a_list), type(a_tuple))

mix_tuple = (1, 5, ['a', 'h'])
print("mix_tuple: ", mix_tuple)
print(mix_tuple[2][1])

#元组元素提取
t_data = ('v', 'c', 'm')
(x, y, z) = t_data
print("x, y, z: ", x, y, z)

#若元组内包含有list，则该list可以更改，list还是list，tuple还是tuple
mix_tuple[2][1] = 'g'
print(mix_tuple)

print("元组转换为列表：", list(mix_tuple))
