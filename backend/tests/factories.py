# coding: utf-8
from app.db import db
from factory import SubFactory
from factory.alchemy import SQLAlchemyModelFactory as Factory
from app.models import TypeCalled, Country, Reason, RecordCalled


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


class RecordCalledFactory(Factory):

    class Meta:
        model = RecordCalled
        sqlalchemy_session = db.session

    type = SubFactory(TypeCalledFactory)
    country = SubFactory(CountryFactory)
    reason = SubFactory(ReasonFactory)
    text = "Como faço para anunciar um item?"
