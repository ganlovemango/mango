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
def index(environ,start_response):
    path = "static/view/index.html"
    html = load_file(path)
    start_response("200 ok",[('ContentType','text/html')])
    return [html]

# 登录页面
def login(environ,start_response):
    path = "static/view/login.html"
    html = load_file(path)
    start_response("200 ok", [('ContentType', 'text/html')])
    return [html]

def do_login(environ,start_response):
    # 获取请求方法类型
    method = environ.get('REQUEST_METHOD','GET')
    if method == 'GET':
        paremeters = environ.get('QUERY_STRING')
        paremeters = parse_qs(paremeters)
        paremeters = {key:value[0] if len(value)==1 else value for key,value in paremeters.items()}
        username = paremeters.get('username')
        password = paremeters.get('password')
        sex = paremeters.get('sex')
        # 业务逻辑处理
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        print(password)
        db = DBHelper('user')
        res = db.where(username=username,password=password).select()
        print(db.sql)
        print(res)
        start_response("200 ok", [('ContentType', 'text/html')])
        if res:
            # 通过验证
            return [b"<html><head><meta http-equiv='refresh' content='0;url=/'></head><body></body></html>"]
        else:
            #跳转登录页面
            return [b"<html><head><meta http-equiv='refresh' content='0;url=/login'></head><body></body></html>"]
            # return [b"<meta http-equiv='refresh' content='0;url=/login'>"]
    else:  #post
        # 参数长度
        contentLength = int(environ.get('CONTENT_LENGTH',0))
        fp = environ.get('wsgi.input')
        paremeters = fp.read(contentLength).decode('utf8')
        paremeters = parse_qs(paremeters)
        paremeters = {key: value[0] if len(value) == 1 else value for key, value in paremeters.items()}
        username = paremeters.get('username')
        password = paremeters.get('password')
        sex = paremeters.get('sex')
        print(paremeters)
        print(username,password,sex)
        # 业务逻辑处理
    start_response("200 ok", [('ContentType', 'text/html')])
    return [b'world']


def register(environ,start_response):
    pass

# 静态资源
def load_static(environ,start_response):
    path = environ.get('PATH_INFO')

    print(path)
    contentType = {
        '.css':'text/css',
        '.js' : 'application/x-javascript',
        '.png': 'image/png',
        '.jpg' : 'image/jpeg',
        '.jpeg' : 'image/jpeg',
        '.bmp':'image/bmp'
    }
    rootPath = environ.get('root_path')
    path = rootPath + path
    # 判断路径是否存在
    if path and os.path.exists(path):
        data = load_file(path)
        # 获取文件后缀
        ext = os.path.splitext(path)[1].lower()  # 文件后缀名
        #判断后缀是否在字典中
        if ext in contentType:
            start_response("200 ok", [('ContentType', contentType[ext])])
        else:
            start_response("200 ok", [('ContentType', 'text/html')])
    else:
        data = b'File Not Found'
        start_response("200 ok", [('ContentType', 'text/html')])
    return [data]


