import random
from datetime import datetime
import os
import hashlib
from urllib.parse import parse_qs  #系统的查询参数解析方法

import jinja2

from DBHelper import DBHelper
from Response import *
from VerifyCode import  VerifyCode



# 读取文件
def load_file(fileName):
    try:
        with open(fileName, 'rb') as fp:
            return fp.read()  # 文件存在
    except Exception as e:
        return b"File not Found"  # 文件不存在

# 静态资源
def load_static(req):
    path = req.environ.get('PATH_INFO')

    print(path)
    contentType = {
        '.css':'text/css',
        '.js' : 'application/x-javascript',
        '.png': 'image/png',
        '.jpg' : 'image/jpeg',
        '.jpeg' : 'image/jpeg',
        '.bmp':'image/bmp'
    }
    rootPath = req.environ.get('root_path')
    path = rootPath + path
    # 判断路径是否存在
    if path and os.path.exists(path):
        data = load_file(path)
        # 获取文件后缀
        ext = os.path.splitext(path)[1].lower()  # 文件后缀名
        #判断后缀是否在字典中
        if ext in contentType:
            req.start_response("200 ok", [('ContentType', contentType[ext])])
        else:
            req.start_response("200 ok", [('ContentType', 'text/html')])
    else:
        data = b'File Not Found'
        req.start_response("200 ok", [('ContentType', 'text/html')])
    return [data]

# 首页
def index(req):
    articles = DBHelper('article').select()
    for article in articles:
        article['publishtime'] = datetime.strftime(article['publishtime'] ,'%Y-%m-%d')
    print(articles)
    return render(req,'blog.html',{'articles':articles})

# 关于我们
def about(req):
    return render(req, 'about.html')

# 注册
def register(req):
    return render(req,'register.html')

# 验证码
def yzm(req):
    vc = VerifyCode()


    data = vc.generate()
    print(vc.code)
    response = Response(req)
    response.set_cookie('yzm', vc.code)
    req.start_response(response.status, response.header)
    return [data]

# 注册处理
def do_register(req):
    code = req.GET.get('code')
    yzm = req.cookie.get('yzm')
    print(code,yzm)
    if code == yzm:
        print("ok")
    else:
        print("failure")
    req.start_response("200 ok", [("ContentType", 'text/html')])
    return [b'register']

# 登录
def login(req):
    return render(req,'login.html')

