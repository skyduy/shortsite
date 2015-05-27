# coding: utf-8

from flask.ext.sqlalchemy import SQLAlchemy

__all__ = ['db', 'SessionMixin']


class SessionMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

db = SQLAlchemy()
