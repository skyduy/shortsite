# coding: utf-8
from _base import db, SessionMixin


class Record(db.Model, SessionMixin):
    __tablename__ = 'url_record'
    id = db.Column(db.INT, primary_key=True)
    raw = db.Column(db.TEXT, nullable=False)
    new = db.Column(db.VARCHAR(30), nullable=False)
    post_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, raw, new):
        self.raw = raw
        self.new = new
