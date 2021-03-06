# Author: DirectorX

import web
import os
import sys

# Stock :: Do not change these settings unless you know what you are doing
app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
views_path = app_path + '/app/views'

render = web.template.render(views_path, globals=globals())
# Base template :: use this if you want to use base template
# render = web.template.render(views_path, base='layout', globals=globals())

# Disallow if you don't want to see web.py's error messages (500)
debug = web.config.debug = True

# Database connection, see web.py documentation for more info
# db = web.database(dbn='mysql', db='dbname', user='user', passwd='passwd', charset=None)
