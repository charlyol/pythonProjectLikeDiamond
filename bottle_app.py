from flask import Flask, render_template
from bottle import default_app, route

import os
@route('/')
def hello_world():

    return render_template(os.path.join(os.path.dirname(__file__), 'src','views','index.html'))

application = default_app()

