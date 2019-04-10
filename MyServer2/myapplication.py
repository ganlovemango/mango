import re
import os
from urls import *
from Request import Request
# 网站入口
def app(environ,start_response):
    path = environ.get('PATH_INFO','/')
    print(path)

    # 站点根目录
    rootPath = os.getcwd()
    environ['root_path'] = rootPath

    #生成请求对象
    req = Request(environ,start_response)

    # 路由
    for pattern,func in patterns:
        # print(re.match(pattern,path),pattern,path)
        if re.match(pattern,path):
            return func(req)

    start_response('200 ok', [('ContentType', 'text/html')])
    # 响应体，是一个可迭代对象，元素必须是字节流字符串
    return ["<h1>404 Not found</h1>".encode('utf8')]
