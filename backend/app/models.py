# coding: utf-8
from datetime import datetime
from app.db import db


class TypeCalled(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(100), nullable=False)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(100), nullable=False)


class Reason(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reason = db.Column(db.String(100), nullable=False)


class RecordCalled(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_called_id = db.Column(db.Integer, db.ForeignKey(TypeCalled.id))
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id))
    reason_id = db.Column(db.Integer, db.ForeignKey(Reason.id))
    currency = db.Column(db.Text, nullable=False)

    created_date = db.Column(db.DateTime, default=datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
