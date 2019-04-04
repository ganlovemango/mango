import pymongo

# 1.连接mongodb
conn = pymongo.MongoClient()
# print(conn)

# 2. 连接数据库
db = conn.student
# print(db)

# 获取查询数据
# data = db.student.find()
# print(data)
# for item in data:
#     print(item)

# 1 insert
# db.course.insert({'cno':'001','cname':'葵花宝典','credit':6})
#
# for item in db.course.find():
#     print(item)

# 2.find
# result = db.student.find({'age':{'$gt':30}})

# 模糊查询
# result = db.student.find({'sname':{'$regex':'^马'}})
# result = db.student.find({'sname':{'$regex':'马'}})


# sort
# result = db.student.find().sort('age',-1)
#limit
result = db.student.find().sort('age',-1).limit(3)
for rec in result:
    print(rec)

#3 关闭连接
conn.close()