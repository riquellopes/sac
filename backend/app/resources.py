# coding: utf:8
import http
from flask import jsonify, make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from app.models import TypeCalled, Country, Reason, RecordCalled
from app.schemas import TypeCalledSchema, CountrySchema, ReasonSchema, RecordCalledSchema

from app.db import db


class RecordCalledListResource(Resource):

    def get(self):
        schema = RecordCalledSchema(many=True)
        data = schema.dump(RecordCalled.query.all())
        return make_response(jsonify(results=data.data))

    @use_args(
        RecordCalledSchema(
            strict=True, only=("type_called_id", "country_id", "reason_id", "text")), locations=("json", ))
    def post(self, recordcalled):
        db.session.add(recordcalled)
        db.session.commit()

        return make_response(
            jsonify(mensagem="record saved successfully"), http.HTTPStatus.CREATED)


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
