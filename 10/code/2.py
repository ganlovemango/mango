from datetime import datetime

import redis

from DBHelper import DBHelper


# 1.在redis中查找
red = redis.StrictRedis(password='111')
sno = input("请输入学号：")
stu = red.hgetall(sno)
# print(stu)
if stu:  #redis有该数据
    print("redis:",stu)
else:
    #2 到mysql中查找
    db = DBHelper('student')
    data = db.where(sno=sno).select()
    # print(data)

    # 将数据加入redis
    #将生日转化为字符串
    # datetime.strftime()
    data[0]['sbirthday'] = data[0]['sbirthday'].strftime("%Y-%m-%d")
    # print(data[0]['sbirthday'])
    red.hmset(sno,data[0])
    print("mysql:",data)


