# coding: utf-8
from app.db import db
from factory.alchemy import SQLAlchemyModelFactory as Factory
from app.models import TypeCalled, Country, Reason


class TypeCalledFactory(Factory):
    class Meta:
        model = TypeCalled
        sqlalchemy_session = db.session

    type = "telefone"


class CountryFactory(Factory):
    class Meta:
        model = Country
        sqlalchemy_session = db.session

    country = "RJ"


class ReasonFactory(Factory):
    class Meta:
        model = Reason
        sqlalchemy_session = db.session

    reason = "dúvidas"
