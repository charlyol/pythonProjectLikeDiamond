# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, Bottle, run, debug, template, redirect, TEMPLATE_PATH
from utils.get_cpu_quota import get_cpu_quota
from src.token.token_py import username_c, token_t
import os

path_directory = os.path.join(os.getcwd(), '..', 'views')
TEMPLATE_PATH.insert(0, path_directory)


@route('/')
def home():
    return template('home_page')


@route('/cpu_quota')
def cpu_quota():
    username = username_c()
    token = token_t()
    quota_info = get_cpu_quota(username, token)
    return quota_info


debug(True)


run(host='localhost', port=8080, reloader=True)
