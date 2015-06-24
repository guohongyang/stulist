# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import reqs


settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static"),"debug":"True" 
}#配置静态文件路径
handlers = [
    (r"/stulist", reqs.StudentListHandler),
    (r"/stuedit/(\d+|new)", reqs.StudentEditHandler),
    (r"/studel/(\d+)", reqs.StudentDelHandler),
    (r"/", reqs.MainHandler),
]

application = tornado.web.Application(handlers, **settings)
application.listen(8888)

if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
