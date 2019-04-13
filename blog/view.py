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
    if req.method == 'GET':
        return render(req,'login.html')
    else:  #post
        phone = req.POST.get('phone')
        code = req.POST.get('code')
        print(phone,code)

        # 从cookie中获取原始的验证码
        # oldCode = req.cookie.get('code')
        # with open('yzm') as fp:
        #     oldcode = fp.read()
        #     print("oldcode",oldcode)

        oldcode = req.cookie.get('code')

        # 数据库查询手机号
        db = DBHelper('user')
        res = db.where(phone=phone).select()
        print(res)
        if res and oldcode == code:
            req.start_response("200 ok", [("ContentType", 'text/html')])
            html = """
            <html>
    <head>
       <meta charset='utf-8'>
       <meta http-equiv='refresh' content='0;url=/login'>
    </head>
    <body>你已通过验证，可以享受贵宾服务</body>
    </html>
            """
            return [html.encode('utf8')]
        else:
            html = """
                        <html>
                <head>
                   <meta charset='utf-8'>
                   <meta http-equiv='refresh' content='0;url=/login'>
                </head>
                <body>你非法用户，请重新登录</body>
                </html>
                        """
            req.start_response("200 ok", [("ContentType", 'text/html')])
            return [html.encode('utf8')]

# 发送短信
def send(req,phone):
    from SMS import SMS
    sms = SMS("成少雷", "SMS_102315005")

    # 验证码
    num = random.randint(10000, 99999)


    para = "{'number':'%d'}" % num
    # 阿里云服务器会修改cookie路径，需要重新吧cookie的path设置/
    res = sms.send(phone, para)

    # 将验证码写入文件
    response = Response(req)
    response.set_cookie('phone', phone)
    response.set_cookie('code', num)

    req.start_response("200 ok", response.header)
    #
    html = b"""
    <html>
    <head>
       <meta charset='utf-8'>
       <meta http-equiv='refresh' content='0;url=/login'>
    </head>
    <body></body>
    </html>
    """
    return [html]