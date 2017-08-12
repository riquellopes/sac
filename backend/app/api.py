# coding: utf-8
from flask_restful import Api
from app import app as application
from app.db import db
from app.resources import (
    TypeCalledListResource, CountryListResource, ReasonListResource, RecordCalledListResource)


def setup_app():
    db.init_app(application)

    api = Api(application, prefix="/v1")
    api.add_resource(TypeCalledListResource, "/type-called/", methods=['GET'])
    api.add_resource(CountryListResource, "/countries/", methods=['GET'])
    api.add_resource(ReasonListResource, "/reasons/", methods=['GET'])
    api.add_resource(RecordCalledListResource, "/recordcalled/", methods=['GET', 'POST'])

    return application


app = setup_app()
