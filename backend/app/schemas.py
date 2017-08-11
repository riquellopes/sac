# coding: utf-8
from marshmallow_sqlalchemy import ModelSchema
from app.models import RecordCalled, TypeCalled, Country, Reason
from app.db import db


class RecordCalledSchema(ModelSchema):

    class Meta:
        model = RecordCalled
        sqla_session = db.session


# Complements.
class TypeCalledSchema(ModelSchema):

    class Meta:
        model = TypeCalled
        sqla_session = db.session


class CountrySchema(ModelSchema):

    class Meta:
        model = Country
        sqla_session = db.session


class ReasonSchema(ModelSchema):

    class Meta:
        model = Reason
        sqla_session = db.session
