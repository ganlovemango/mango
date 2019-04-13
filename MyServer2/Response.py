import jinja2
from settings import *
# 生成响应对象
class Response:
    def __init__(self,req):
        self.req = req
        self.header = []  # 响应头
        self.status = "200 ok"  #状态行

    # 加载模板文件
    def load(self,path,**kwargs):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATEPATH))
        template = env.get_template(path)  # 加载模板
        # 渲染模板文件，生成html源代码
        html = template.render(**kwargs)
        self.header.append(("ContentType",'text/html'))
        self.req.start_response(self.status,self.header)
        return [html.encode('utf8')]
    # cookie
    def set_cookie(self,key,value,expired=24*3600*3,path='/'):
        """
        username=tom;Max-Age=3
        :param key: 键
        :param value: 值
        :param expired: 过期时间，以秒为单位
        :return:
        """
        cs = key + "=" +str(value) + ";"
        if expired:  #如果设置了过期时间
            cs += "Max-Age=" + str(expired)
        cs += "path="+path

        self.header.append(('Set-Cookie',cs))


# render
def render(req,file,data={}):
    """

    :param req:  请求对象
    :param file: 文件路径
    :param data: 字典参数
    :return: 可迭代对象
    """
    response = Response(req)
    return  response.load(file,**data)