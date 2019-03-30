# 1.字典
# some_dict = {}
# some_dict[5.5] = "雷哥的支付宝贼6"
# some_dict[5.0] = "雷哥天天偷能量"
# some_dict[5] = "我永远偷不到雷哥的能量！"
#
# print(some_dict[5.5])
# print(some_dict[5.0])
# print(some_dict[5])
# res = hash(5) == hash(5.0)
# print(res)






# 2.生成器
# array = [1, 8, 15]
# g = (x for x in array if array.count(x) > 0)
# array = [2, 8, 22]
#
# print(list(g))



# 3.列表迭代式
# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]
# for idx, item in enumerate(list_1):
# 	del item
# for idx, item in enumerate(list_2):
# 	list_2.remove(item)
# for idx, item in enumerate(list_3[:]):
# 	list_3.remove(item)
# for idx, item in enumerate(list_4):
# 	list_4.pop(idx)
#
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)


#.+ 和 +=
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]

print(a)
print(b)

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]

print(a)
print(b)