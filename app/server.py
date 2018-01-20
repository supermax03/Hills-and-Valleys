import tornado.ioloop
import json
from utils.utils import convertinput
from tornado.web import *
from business.hillsandvalleys import getgroundinfo


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        info_app = {

            "Name": "Hills and Valleys",
            "Author": "Maximiliano Bordon",
            "Version": "1.0",
            "Comments": "An application that counts hills and valleys given an array with numeric values representing the ground"
        }
        self.write(json.dumps(info_app))


class GroundInfoHandler(tornado.web.RequestHandler):
    @tornado.web.addslash
    def get(self):
        more_info = {
            'Examples': {1: {"input": "http://localhost:port/groundinfo/1,0,1",
                             "output": "Hills->2 Valleys->1"
                             },
                         2: {"input": "http://localhost:port/groundinfo/1,1,1",
                             "output": "Hills->0 Valleys->0"}
                         }

        }
        self.write(json.dumps(more_info))


class SolutionHandler(RequestHandler):

    def get(self, groundconditions):
        hills, valleys = getgroundinfo(convertinput(groundconditions))
        result = {'hills': hills,
                  'valleys': valleys}
        self.write(json.dumps(result))


app = Application([
    (r'/', MainHandler),
    (r'/info/?', GroundInfoHandler),
    (r'/groundinfo/(.*)', SolutionHandler),

])
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
