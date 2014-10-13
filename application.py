#!/usr/bin/env python2
# Author: DirectorX

import web
import app.controllers
from app.config import debug

urls = (
	'/(.*)',	'app.controllers.hello.world',
)

App = web.application(urls, globals())

if __name__ == "__main__":
	App.run()
