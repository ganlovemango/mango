import os
# 数据库链接参数
db = {
    'host': 'localhost',  # 服务器地址
    'user': 'root',  # 帐号
    'password' :'123',  # 密码
    'db' :'student',  # 数据库名称
    'port' : 3306,  # 端口，默认是3306
    'charset' : 'utf8'  #
}

#基础路径
BASEPATH = os.getcwd()

# 模板路径
TEMPLATEPATH =  os.path.join(BASEPATH,'templates')


