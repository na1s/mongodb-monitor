import web
class todo:
    def __init__(self):
        self.title="speed"
        self.id = 42
def get_todos():
    return [todo()]
