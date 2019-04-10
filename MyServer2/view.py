import os
import hashlib
from urllib.parse import parse_qs  #系统的查询参数解析方法

from DBHelper import DBHelper

# 处理模块

# 读取文件
def load_file(fileName):
    try:
        with open(fileName, 'rb') as fp:
            return fp.read()  # 文件存在
    except Exception as e:
        return b"File not Found"  # 文件不存在

# 首页
def index(req):
    path = "static/view/index.html"
    html = load_file(path)
    req.start_response("200 ok",[('ContentType','text/html')])
    return [html]

# 登录页面
def login(req):
    path = "static/view/login.html"
    html = load_file(path)
    req.start_response("200 ok", [('ContentType', 'text/html')])
    return [html]

def do_login(req):
    # 获取请求方法类型
    if req.method == 'GET':
        username = req.GET.get('username')
        password = req.GET.get('password')
        sex = req.GET.get('sex')
        print(username,password)
        # 业务逻辑处理
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        print(password)
        db = DBHelper('user')
        res = db.where(username=username,password=password).select()
        print(db.sql)
        print(res)
        req.start_response("200 ok", [('ContentType', 'text/html')])
        # if res:
        #     # 通过验证
        #     return [b"<html><head><meta http-equiv='refresh' content='0;url=/'></head><body></body></html>"]
        # else:
            #跳转登录页面
            # return [b"<html><head><meta http-equiv='refresh' content='0;url=/login'></head><body></body></html>"]
            # return [b"<meta http-equiv='refresh' content='0;url=/login'>"]
        return [b'dologin']
    else:  #post
        username = req.POST.get('username')
        password = req.POST.get('password')
        sex = req.POST.get('sex')
        print(username,password,sex)
        # 业务逻辑处理
    req.start_response("200 ok", [('ContentType', 'text/html')])
    return [b'world']


def register(req):
    pass

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


