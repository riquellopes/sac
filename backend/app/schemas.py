# coding: utf-8
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from app.models import RecordCalled, TypeCalled, Country, Reason
from app.db import db


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


class RecordCalledSchema(ModelSchema):
    type = fields.Nested(TypeCalledSchema)
    country = fields.Nested(CountrySchema)
    reason = fields.Nested(ReasonSchema)

    class Meta:
        model = RecordCalled
        sqla_session = db.session
