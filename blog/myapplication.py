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
        result = re.match(pattern, path)
        if result:
            if func.__code__.co_argcount == 1:
                return func(req)
            elif func.__code__.co_argcount == len(result.groups()) + 1:
                return func(req,*result.groups())
            else:
                start_response('200 ok', [('ContentType', 'text/html')])
                return ["服务器内部错误，请检查代码".encode('utf8')]
    start_response('200 ok', [('ContentType', 'text/html')])
    # 响应体，是一个可迭代对象，元素必须是字节流字符串
    return ["<h1>404 Not found</h1>".encode('utf8')]
