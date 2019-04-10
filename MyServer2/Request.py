# 封装请求类，完成GET、POST参数解析
from urllib.parse import parse_qs

class Request:
    def __init__(self,environ,start_response):
        self.environ = environ  # 环境变量
        self.start_response = start_response  #生成请求头的方法

        #请求方法：
        self.method = environ.get('REQUEST_METHOD','GET')

        #请求路径
        self.path = environ.get('PATH_INFO','/')

        #GET参数字典
        self.GET = self.__get_parameters()

        #POST参数字典
        self.POST = self.__post_parameters()

    def __get_parameters(self):
        paremeters = self.environ.get('QUERY_STRING')
        paremeters = parse_qs(paremeters)
        paremeters = {key: value[0] if len(value) == 1 else value for key, value in paremeters.items()}
        return paremeters

    def __post_parameters(self):
        #参数长度，按字节计算
        contentLength = int(self.environ.get('CONTENT_LENGTH', 0))

        # post的指针
        fp = self.environ.get('wsgi.input')
        paremeters = fp.read(contentLength).decode('utf8')
        paremeters = parse_qs(paremeters)
        paremeters = {key: value[0] if len(value) == 1 else value for key, value in paremeters.items()}
        return paremeters