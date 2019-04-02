#pymysql操作mysql数据库
import pymysql

import settings   #配置文件

# 1.链接数据库服务器
conn = pymysql.Connect(**settings.db)
print(conn)
# 2 创建游标
# 默认的游标获取的记录是元组套元组（（）,（）,....）
# DictCursor 返回的数据是列表套字典[{}]
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 3.执行sql语句
sno = input("请输入学号：")

# 通过构造特殊的输入串，构造一个永真条件，绕过判断条件，非法获取数据这就是sql注入
"""
请输入学号：ksdkfksdf' or '1
select sno,sname,sbirthday,class from student where sno='ksdkfksdf' or '1'

"""
# sql = "select sno,sname,sbirthday,class from student where sno='%s'"%sno

# 防止sql注入

# 1.通过escape_string将字符中特殊字符转意
# sno = pymysql.escape_string(sno)
"""
请输入学号：ksdkfksdf' or '1
select sno,sname,sbirthday,class from student where sno='ksdkfksdf\' or \'1'
"""
# sql = "select sno,sname,sbirthday,class from student where sno='%s'"%sno

# 通过execute（sql,args)
sql = "select sno,sname,sbirthday,class from student where sno=%s"

res = cursor.execute(sql,(sno,))   #返回值是记录数
print(res)
print(cursor._executed)
# 4.获取数据
#获取一条数据
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# #如果取不到记录，返回None
# print(cursor.fetchone())

# 取多条记录
# data = cursor.fetchmany(6)
# for rec in data:
#     print(rec[1],rec[-1])

#获取所有记录
data = cursor.fetchall()
print(data)

#查看sql语句
# print(cursor._executed)

# 5.关闭链接和游标
cursor.close()
conn.close()