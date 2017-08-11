# coding: utf:8
from flask import jsonify, make_response
from flask_restful import Resource
from app.models import TypeCalled, Country, Reason, RecordCalled
from app.schemas import TypeCalledSchema, CountrySchema, ReasonSchema, RecordCalledSchema


class RecordCalledListResource(Resource):

    def get(self):
        schema = RecordCalledSchema(many=True)
        data = schema.dump(RecordCalled.query.all())
        return make_response(jsonify(results=data.data))


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
