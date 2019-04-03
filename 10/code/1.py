import redis

# 1.连接redis服务器
red = redis.StrictRedis(password='111')

# string
#设置key
# res = red.set('name','范冰冰')  # 成功返回True，否则返回False
# name = red.get('name')  #返回值是字节流字符串，需要解码
# print(name.decode('utf8'))

# #mset
# red.mset({'age':20,'sex':'男'})
# #mget
# print(red.mget('age','sex'))

# hash
# red.hset('p1','hobby','睡觉')
# red.hset('p1','eat','美食')
print(red.hget('p1','hobby').decode('utf8'))
