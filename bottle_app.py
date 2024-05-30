from flask import Flask
from bottle import default_app, route, static_file
import os


@route('/')
def hello_world():
    
    return static_file('index.html',os.path.join(os.path.dirname(__file__), 'src','views'))

application = default_app()

