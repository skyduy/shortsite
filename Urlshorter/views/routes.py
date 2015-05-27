# coding: utf-8
"""
    路由
    ~~~~~~~~~~
    :author  Dultty <cuteuy@gmail.com>
"""
from flask import Blueprint

home = Blueprint('home', __name__)
from resources.home import Home, Jump
home_view = Home.as_view('home_view')
jump_view = Jump.as_view('jump_view')
home.add_url_rule('/', view_func=home_view)
home.add_url_rule('<string:suffix>', view_func=jump_view)

