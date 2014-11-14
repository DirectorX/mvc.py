#!/usr/bin/env python2
# Author: DirectorX

import web
import app.controllers
from app.config import debug, routes

App = web.application(routes.urls, globals())

if __name__ == "__main__":
	App.run()
