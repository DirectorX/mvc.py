# Author: DirectorX

from app.controllers import Controller


class world(Controller):
    def GET(self, name):
        if not name:
            name = 'World'
        return self.render.helloworld(name)
