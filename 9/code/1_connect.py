#pymysql操作mysql数据库
import pymysql

# 1.链接数据库服务器
conn = pymysql.Connect(
                        host='localhost',  #服务器地址
                        user='root',       #帐号
                        passwd='123',      #密码
                        db='homework',     # 数据库名称
                        port=3306,         # 端口，默认是3306
                        charset='utf8'     # 设置字符集
                        )
# print(conn)
# 2 创建游标
# 默认的游标获取的记录是元组套元组（（）,（）,....）
cursor = conn.cursor()

# 3.执行sql语句
sql = "select sno,sname,sbirthday,class from student"
res = cursor.execute(sql)   #返回值是记录数
print(res)

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