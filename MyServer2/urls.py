import view
# 路由规则表
patterns = [(r'^/$', view.index),
           (r'^/login$', view.login),
            (r'^/static',view.load_static),
            (r'^/register$',view.register),
            (r'^/doLogin$',view.do_login),
            (r'^/studentlist$',view.student_list),
            (r'^/studentdetail/(\d+)$',view.student_detail),
            (r'^/logout$',view.logout),
           ]