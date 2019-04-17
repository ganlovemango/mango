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
            # ajax
            (r'^/showajax$',view.show_ajax),
            (r'^/showajax1$',view.show_ajax1),
            (r'^/ajax1',view.do_ajax1),
            (r'^/getusername$',view.check_username),
            (r'^/showprovince$',view.show_province),
            (r'^/province$',view.get_province),
           ]