# 自己的应用
# def app(environ,start_response):
#     # print(environ)
#     # for key in environ:
#     #     print(key,'-'*5,environ[key])
#     #生成响应头
#     # 第一个参数 状态描述
#     #响应头信息，需要传过来一个列表，每一个元素格式（键,值）
#     start_response('200 ok', [('ContentType', 'text/html')])
#     path = environ.get('PATH_INFO','/')
#     print(path)
#
#     if path == '/':  #请求的首页
#         with open('static/view/index.html','rb') as fp:
#             return [fp.read()]
#     elif path == '/login':  # 登录页面
#         with open('static/view/login.html','rb') as fp:
#             return [fp.read()]
#
#     # 响应体，是一个可迭代对象，元素必须是字节流字符串
#     return ["<h1>404 Not found</h1>".encode('utf8')]
import re
import os
from urls import *

def app(environ,start_response):
    path = environ.get('PATH_INFO','/')
    print(path)

    # 站点根目录
    rootPath = os.getcwd()
    environ['root_path'] = rootPath
    # 路由
    for pattern,func in patterns:
        # print(re.match(pattern,path),pattern,path)
        if re.match(pattern,path):
            return func(environ,start_response)

    #路由
    # if path == '/':  # 请求的首页
    #     return index(start_response)
    # elif path == '/login':  # 登录页面
    #     return login(start_response)

    start_response('200 ok', [('ContentType', 'text/html')])
    # 响应体，是一个可迭代对象，元素必须是字节流字符串
    return ["<h1>404 Not found</h1>".encode('utf8')]
