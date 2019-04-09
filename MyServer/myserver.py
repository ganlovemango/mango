from wsgiref.simple_server import make_server
from myapplication import  app

# 创建的服务器
# 第一个参数：服务器地址
# 第二个参数：端口，不要用80
# 第三个参数：自己的web网站,必须是可调用对象
server = make_server('localhost',9000,app)
print("服务器启动......")
server.serve_forever()
