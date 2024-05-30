from flask import Flask
from bottle import default_app, route, static_file
import os


@route('/')
def hello_world():
<<<<<<< HEAD

    return static_file('index.html',os.path.join(os.path.dirname(__file__), 'src','views'))
=======
    
    return static_file('index.html',root=os.path.join(os.path.dirname(__file__), 'src','views'))
>>>>>>> c1db2041de877df89c4eb78d0a5474d8dc1d4f4b

application = default_app()

