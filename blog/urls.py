import view
# 路由规则表
patterns = [(r'^/$', view.index),
            (r'^/static',view.load_static),
            (r'^/about$',view.about),
            (r'^/register$',view.register),
            (r'/verifycode',view.yzm),
            (r'/doregister',view.do_register),
            (r'^/login$', view.login),
            (r'^/sms/(\d+)$',view.send),

           ]