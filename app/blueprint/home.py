#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc
from app.model.base import User

homeBlueprint = Blueprint(
    'home',
    __name__
)

@homeBlueprint.route('/')
@homeBlueprint.route('/index')
def index():
    return render_template('index.html')
