""" Basic todo list using webpy 0.3 """
import json
from bson import *
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/charts', 'Charts',
    '/conf/v3/(.+)', 'Conf',
    '/ping/v1/(.+)', 'Ping',
)


### Templates
render = web.template.render('templates', base='base')


class Index:
    def GET(self):
        """ Show page """
        todos = model.get_todos()
        return render.index(todos)


class Charts:
    def GET(self):
        """ Show page """
        web.header('Content-Type', 'application/json')
        todos = [
            {"title": '2008', "value": 20},
            {"title": '2009', "value": 10},
            {"title": '2010', "value": 5},
            {"title": '2011', "value": 5},
            {"title": '2012', "value": 20}
        ]
        return json.dumps(todos)


class Conf:
    def GET(self,id):
        web.header('Content-Type', 'application/json')
        todos = {"disableDbstats": False, "hosts": [
            {"hostname": "127.0.0.1", "hostKey": "127.0.0.1:27017", "munin": True, "getLogs": False,
             "sslEnabled": False, "uri": "mongodb://127.0.0.1:27017", "id": "3b2432a9a24815be0aaaafbba46617fc",
             "profiler": True, "port": 27017}]}
        b = BSON.encode(todos)
        return b

class Ping:
    def POST(self,id):
        data = web.data()
        b = BSON.decode(data)
        return
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()