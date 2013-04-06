""" Basic todo list using webpy 0.3 """
import json
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/charts', 'Charts',
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
            { "title": '2008', "value": 20 },
            { "title": '2009', "value": 10 },
            { "title": '2010', "value": 5 },
            { "title": '2011', "value": 5 },
            { "title": '2012', "value": 20 }
        ]
        return json.dumps(todos)





app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()