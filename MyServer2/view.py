import json
import os
import hashlib
from urllib.parse import parse_qs  #系统的查询参数解析方法

import jinja2
import pymysql

from DBHelper import DBHelper
from Response import *

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
    return render(req,'index.html',{'cookie':req.cookie})

# 登录页面
def login(req):
    path = "static/view/login.html"
    html = load_file(path)
    req.start_response("200 ok", [('ContentType', 'text/html')])
    return [html]

#退出登录
def logout(req):
    response= Response(req)
    response.set_cookie('uid','',expired=-1)
    response.set_cookie('username','',expired=-1)
    response.header.append(('ContentType','text/html'))
    response.req.start_response("200 ok",response.header)
    return [b"<html><head><meta http-equiv='refresh' content='0;url=/login'></head><body></body></html>"]


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
        response = Response(req)
        if res:
            # 通过验证
            uid = res[0]['uid']
            username = res[0]['username']
            response.set_cookie('uid',uid)
            response.set_cookie('username',username)
            response.header.append(("ContentType",'text/html'))
            response.req.start_response("200 ok",response.header)
            return [b"<html><head><meta http-equiv='refresh' content='0;url=/'></head><body></body></html>"]
        else:
            # 跳转登录页面
            return [b"<html><head><meta http-equiv='refresh' content='0;url=/login'></head><body></body></html>"]
            # return [b"<meta http-equiv='refresh' content='0;url=/login'>"]
        # return [b'dologin']
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


# 学生列表
# def student_list(req):
#     db = DBHelper('student')
#     data = db.select()
#     print(data)
#     # 加载学生列表源文件
#     html = load_file('static/view/studentlist.html').decode('utf8')
#     stu = ""
#     # 生成行
#     for rec in data:
#         stu += "<tr><td>"+rec['sno']+"</td><td>"+rec['sname']+"</td></tr>"
#
#     html = html.format(student=stu)  #格式化字符串
#     print(html)
#     req.start_response("200 ok", [('ContentType', 'text/html')])
#     return [html.encode('utf8')]
# def student_list(req):
#     db = DBHelper('student')
#     data = db.select()
#     # 实例化加载对象
#     env = jinja2.Environment(loader=jinja2.FileSystemLoader("./static/view"))
#     template = env.get_template('studentlist.html')  #加载模板
#     # print(template)
#     # 渲染模板文件，生成html源代码
#     html = template.render(title='1902学生列表',data=data)
#     # print(html)
#     req.start_response("200 ok", [('ContentType', 'text/html')])
#     return [html.encode('utf8')]

def student_list(req):
    db = DBHelper('student')
    data = db.select()
    return render(req,'studentlist.html',{'title':'1902','data':data})

def student_detail(req,sno):
    # sno = req.GET.get('sno')
    print(sno)
    db = DBHelper('student')
    student = db.where(sno=sno).select()
    if student:
        student = student[0]
        return render(req,'studentdetail.html',{'title':student['sname'],'data':student})
    else:
        return render(req,'404.html')

# ajax
def show_ajax(req):
    return  render(req,'ajax1.html')
def show_ajax1(req):
    return render(req, 'ajax2.html')
def do_ajax1(req):
    username = req.GET.get('username')
    print(username)
    res = {'msg':'数据已收到','code':'1'}
    res = json.dumps(res)
    print(res)
    req.start_response("200 ok",[('ContentType','application/json')])
    return [res.encode('utf8')]

# 检查用户名是否重名
def check_username(req):
    if req.method == 'GET':
        username = req.GET.get('username')
    else:
        username = req.POST.get('username')
    # 查询数据库
    db = DBHelper('user')
    res = db.where(username=username).select()
    if res:
        data = {'code':1,'msg':'用户名不可用'}
    else:
        data = {'code':0,'msg':'用户名可用'}
    req.start_response("200 ok",[("ContentType","application/json")])
    print(res)
    return [json.dumps(data).encode('utf8')]

def show_province(req):
    return render(req, 'prevince.html')

def get_province(req):
    db = DBHelper('region')
    data = db.where(pid='0').select()
    print(db.sql)
    print(data)

    req.start_response("200 ok", [("ContentType", "application/json")])
    return [json.dumps(data).encode('utf8')]

def show_test(req):
    return render(req, 'test1.html')

# 分页
def show_page(req):
    return render(req, 'page.html')

def get_data(req):
    # 页数
    page = int(req.GET.get('page',1))
    # 第一页的页号
    first = int(req.GET.get('first',1))

    # 1.每页显示数据条数 10
    # 2.当前请求的是第几页
    # 3.获取表中总记录数
    # 4.计算总页数: 总记录数 /  每页显示数据条数
    # 5.当前页显示的记录: limit 10*(page-1),10

    db = DBHelper('region')
    data = db.limit(10*(page-1),10).select()
    print(data)
    print(db.sql)

    # 计算总记录数
    total = db.fields('count(*) num').select()
    if total:
        total = total[0]['num']
    countOfPage = total // 10  #总页数

    # 默认每页显示10个页号
    pageNo = {'first': first, 'last': first + 9}
    if page - 5 < 0:
        pageNo['first'] = 1
        pageNo['last'] = 10
    elif page + 4 > pageNo['last']:
        pageNo['last'] = page + 4
        pageNo['first'] = pageNo['last'] - 9
    data.append(pageNo)
    req.start_response("200 ok", [("ContentType", "application/json")])
    return [json.dumps(data).encode('utf8')]