# coding: utf:8
from flask import jsonify, make_response
from flask_restful import Resource
from app.models import TypeCalled, Country, Reason
from app.schemas import TypeCalledSchema, CountrySchema, ReasonSchema


class RecordCalledResource(Resource):
    pass


# Complements.
class TypeCalledListResource(Resource):

    def get(self):
        schema = TypeCalledSchema(many=True)
        data = schema.dump(TypeCalled.query.all())
        return make_response(jsonify(results=data.data))


class CountryListResource(Resource):

    def get(self):
        schema = CountrySchema(many=True)
        data = schema.dump(Country.query.all())
        return make_response(jsonify(results=data.data))


class ReasonListResource(Resource):

    def get(self):
        schema = ReasonSchema(many=True)
        data = schema.dump(Reason.query.all())
        return make_response(jsonify(results=data.data))
