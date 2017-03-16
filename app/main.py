#!/usr/bin/python
#coding=utf-8
import time
from logging import FileHandler,WARNING,DEBUG
from random import random
from os import urandom
from math import ceil

from flask import Flask,request,render_template,jsonify,redirect,url_for,make_response,g
from flask import session as flaskSession
from sqlalchemy import distinct,desc

from blueprint.home import homeBlueprint
from model.base import Session


def create_app():
    app = Flask(__name__)
    app.secret_key = '\x14:\xe3\x1aB\xc5|\x10iQ\xd9 \xdf\xce\x19\x83\xd3\xb7s\x97\xee(T\xb8\xb25\xd3\xd1\xe1NJ\x92'

    # 日志记录
    fileHandler = FileHandler('app/log/warning.log')
    fileHandler.setLevel(WARNING)
    app.logger.addHandler(fileHandler)

    # 注册蓝图
    app.register_blueprint(baseBlueprint)

    @app.before_request
    def before_request():
        g.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        g.dbSession = Session()

        if 'username' not in request.cookies and request.cookies.get('username') != flaskSession['username']:
            return render_template('login.html')

    @app.teardown_request
    def teardown_request(exception):
        g.dbSession.close()

    @app.errorhandler(500)
    def pageNotFound(error):
        return render_template('error/500.html'),500

    @app.errorhandler(404)
    def pageNotFound(error):
        return render_template('error/404.html'),404

    @app.route('/')
    @app.route('/index')
    def index():
        return redirect(url_for('home.index'))
    
    return app
