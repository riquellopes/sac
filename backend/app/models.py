# coding: utf-8
from datetime import datetime
from app.db import db


class TypeCalled(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(100), nullable=False, unique=True)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(100), nullable=False, unique=True)


class Reason(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reason = db.Column(db.String(100), nullable=False, unique=True)


class RecordCalled(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_called_id = db.Column(db.Integer, db.ForeignKey(TypeCalled.id), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id), nullable=False)
    reason_id = db.Column(db.Integer, db.ForeignKey(Reason.id), nullable=False)
    text = db.Column(db.Text, nullable=False)

    # relationships
    type = db.relationship("TypeCalled", foreign_keys=[type_called_id])
    country = db.relationship("Country", foreign_keys=[country_id])
    reason = db.relationship("Reason", foreign_keys=[reason_id])

    created_date = db.Column(db.DateTime, default=datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
