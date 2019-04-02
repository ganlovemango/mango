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
sname = input("请输入姓名：")
try:
    # 使用pymysql进行增加、删除、修改是自动开启事务的，必须手动commit或rollback
    sql = "insert into student(sno,sname) values('{}','{}')".format(sno,sname)
    # print(sql)
    res = cursor.execute(sql)   # 返回值是受影响的行数
    if res > 0:
        conn.commit()  #提交的数据库
        # print(cursor.lastrowid)  #获取自增主键的值
    else:
        conn.rollback()
    # #查看sql语句
    print(cursor._executed)
    print(res)
except Exception as e:
    print(e)
finally:
    # 5.关闭链接和游标
    cursor.close()
    conn.close()



