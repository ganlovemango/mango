#数据库辅助类
import pymysql

import settings


"""
db = DBHelper()
db.insert({})
db.where().delete()
db.where().update()
db.fields().where().limit().orderby().select()
db.where().fields().select()


"SELECT {FIELDS} FROM {TABLE} {WHERE} {GROUPBY} {HAVING} {ORDERBY} {LIMIT}"
"""

class DBHelper:
    def __init__(self,table):
        self.table = table  # 表名
        self.conn = pymysql.Connect(**settings.db)    # 链接数据库
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)  #游标
        self.__init_options()  #初始化查询参数
        self.sql = ''

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 参数字典初始化
    def __init_options(self):
        self.options = {
            'table'   : self.table,
            'fields'  : '*',     #字段列表
            'where'   : '',      # where条件
            'groupby' : '',      # group by子句
            'having'  : '',      # having
            'orderby' : '',      # order by
            'limit'   : ''       # limit
        }

    def limit(self,*args):
        if len(args) <= 0:
            return self
        args = [str(value) for value in  args[:2]]
        self.options['limit'] = " limit " + ','.join(args)
        return self


    def orderby(self,*args):
        if len(args) <= 0:
            return self
        self.options['orderby'] = " order by " + ','.join(args)
        return self

    def having(self,**kwargs):
        """

        :param kwargs: num__gt=2  => num > 2
        :return:
        """
        if len(kwargs) <= 0:
            return self
        if self.options['having']:  #存在having子句
            self.options['having'] += ' and '
        else:
            self.options['having'] = " having "
        ops = {
            'gt':">",
            'ge':'>=',
            'lt':'<',
            'le':'<=',
            'neq':'!='
        }
        # 拼接条件
        for key,value in kwargs.items():
            op = key.split("__")   #将key分割为两部分
            if isinstance(value,str):
                if len(op) > 1:  # 运算符不是=
                    #op[0] 字段名   op[1]运算符
                    self.options['having'] += op[0] + ops[op[1]] + "'" + pymysql.escape_string(value) + "' and "
                else:
                    self.options['having'] += op[0] +" = '" + pymysql.escape_string(value) + "' and "
            else:
                if len(op)>1:
                    self.options['having'] += op[0] + ops[op[1]] +str(value) + " and "
                else:
                    self.options['having'] += op[0] + " = " + str(value) + " and "
        self.options['having'] = self.options['having'].rstrip("and ")
        return self


                #分组
    def groupby(self,*args):
        """

        :param args: 分组参数  groupby('sno',' sex desc')
        :return:
        """
        if len(args) <=0:  #不传参数
            return self
        self.options['groupby'] = " group by " + ','.join(args)
        return self
    # 字段列表
    def fields(self,*args):
        args = [str(value) for value in args]
        self.options['fields'] = ','.join(args)
        return self
    def where(self,**kwargs):
        """
        {'sno':'105','sex':'男'}
        :param kwargs:
        :return:
        """
        if len(kwargs) <= 0:  #没有传参数
            return self

        # 有where条件
        if 'where' in self.options['where']:
            self.options['where'] += ' and '  #默认是and连接
        else:  # where条件为空
            self.options['where'] = " where "
        #拼接查询条件
        for key,value in kwargs.items():
            if isinstance(value,str):
                self.options['where'] += key + " = '" + pymysql.escape_string(value) + "' and "
            else:
                self.options['where'] += key + " = " + str(value) + " and "
        self.options['where'] = self.options['where'].rstrip("and ")  # 去掉末尾的and
        print(self.options['where'])
        return self

    def select(self):
        sql = "SELECT {fields} FROM {table} {where}  {groupby} {having}  {orderby} {limit}"
        sql = sql.format(**self.options)
        return self.query(sql)

    def query(self,sql):
        self.sql = sql  # 保留sql语句
        # 初始化查询参数字典
        self.__init_options()
        try:
            res = self.cursor.execute(sql)
            if res > 0:
                return self.cursor.fetchall()
            else:
                return None
        except Exception as e:
            print(e)
            return None

    # insert 一条就记录
    def insert(self,data):
        """

        :param data: 字典，代表一条记录，键是字段名
        :return:
        """
        # 1 如果字典的值是字符串，两边添加单引号
        self.__add_quote(data)

        # 生成字段列表和值列表
        keys = ''
        values = ''
        for key,value in data.items():
            keys += key + ','
            values += str(value) + ','
        keys = keys.rstrip(',')
        values = values.rstrip(',')
        self.options['fields'] = keys
        self.options['value'] = values

        sql = "INSERT INTO {table} ({fields})  VALUES({value})".format(**self.options)
        print(sql)
        return self.execute(sql)

    def execute(self,sql):
        self.sql = sql
        self.__init_options()
        try:
            res = self.cursor.execute(sql)
            if res > 0:
                self.conn.commit()
                return True
            else:
                self.conn.rollback()
                return False
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False


    # 给字符串两边添加单引号
    def __add_quote(self,data):
        for key in data:
            if isinstance(data[key],str):
                data[key] = "'" + data[key] +"'"

if __name__ == "__main__":
    db = DBHelper('student')
    # data = db.where(**{'sno':'105'}).where(ssex='男').where().select()
    # data = db.where(ssex='男').fields('sno,sname').where().select()
    # data = db.fields('ssex,count(*) num').having(num__gt=2).groupby('ssex').select()
    # data = db.orderby('sname','ssex desc').limit(1,3).select()
    # print(data)
    # print(db.sql)
    # print(db.__dict__)
    # db.insert({'sno':'112','sname':'tom','sbirthday':'2019-4-2'})