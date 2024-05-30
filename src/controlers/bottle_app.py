# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, Bottle, run, debug, template, redirect, TEMPLATE_PATH
from utils.get_cpu_quota import get_cpu_quota
import os

path_directory = os.path.join(os.getcwd(), '..', 'views')
TEMPLATE_PATH.insert(0, path_directory)


@route('/')
def home():
    return template('home_page')


@route('/cpu_quota')
def cpu_quota():
    username = 'CharlyOlinger'
    token = '6c662ac265f1f9a47fa07f027bc52313e809e636'
    quota_info = get_cpu_quota(username, token)
    return quota_info


debug(True)


run(host='localhost', port=8080, reloader=True)
