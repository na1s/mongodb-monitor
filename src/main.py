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
        todos = [{"name":m.title} for m in model.get_todos()]
        return json.dumps(todos)




app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()