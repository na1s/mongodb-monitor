""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        return render.index(todos)





app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()