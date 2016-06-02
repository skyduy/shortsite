# coding: utf-8
from _base import db


def register_database(app):
    from const import (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % \
                                            (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    db.init_app(app)
