# 自己的应用
def app(environ,start_response):
    # print(environ)
    # for key in environ:
    #     print(key,'-'*5,environ[key])
    start_response('200 ok', [('ContentType', 'text/html')])
    path = environ.get('PATH_INFO','/')
    print(path)

    if path == '/':  #请求的首页
        with open('static/view/index.html','rb') as fp:
            return [fp.read()]
    elif path == '/login':  # 登录页面
        with open('static/view/login.html','rb') as fp:
            return [fp.read()]

    return ["<h1>404 Not found</h1>".encode('utf8')]
