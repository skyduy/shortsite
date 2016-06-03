# coding: utf-8

"""
    App入口
    ~~~~~~~~~~

    :author Skyduy <cuteuy@gmail.com> <http://skyduy.me>

"""

from flask import Flask

from models import init_database


def create_app(**config):
    """
    创建并初始化一个 Flask App
    :param
    :return
    """
    app = Flask(
        __name__,
        template_folder='views/templates'
    )

    register_config(app, config)
    register_database(app)
    register_routes(app)
    return app


def register_config(app, config):
    """注册相关配置"""
    if config.get('debug') is True:
        app.debug = True


def register_database(app):
    db = init_database(app)
    with app.app_context():
        db.create_all()


def register_routes(app):
    """向 Flask app 注册路由"""
    from Urlshorter.views.routes import home
    app.register_blueprint(home, url_prefix='/')

if __name__ == '__main__':
    create_app(debug=True).run()
