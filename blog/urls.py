import view
# 路由规则表
patterns = [(r'^/$', view.index),
            (r'^/static',view.load_static),
            (r'^/login$', view.login),
           ]