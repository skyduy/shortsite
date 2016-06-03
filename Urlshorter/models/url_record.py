# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class SessionMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Record(db.Model, SessionMixin):
    __tablename__ = 'url_record'
    id = db.Column(db.INT, primary_key=True)
    raw = db.Column(db.VARCHAR(200), nullable=False, unique=True)
    new = db.Column(db.VARCHAR(4), nullable=False, unique=True)
    post_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, raw, new):
        self.raw = raw
        self.new = new
