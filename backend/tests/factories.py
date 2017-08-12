# coding: utf-8
from app.db import db
from factory import SubFactory, Sequence
from factory.alchemy import SQLAlchemyModelFactory as Factory
from app.models import TypeCalled, Country, Reason, RecordCalled


class TypeCalledFactory(Factory):
    class Meta:
        model = TypeCalled
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    type = Sequence(lambda n: "telefone %03d" % n)


class CountryFactory(Factory):
    class Meta:
        model = Country
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    country = Sequence(lambda n: "RJ %03d" % n)


class ReasonFactory(Factory):
    class Meta:
        model = Reason
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    reason = Sequence(lambda n: "dúvidas %03d" % n)


class RecordCalledFactory(Factory):

    class Meta:
        model = RecordCalled
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    type = SubFactory(TypeCalledFactory)
    country = SubFactory(CountryFactory)
    reason = SubFactory(ReasonFactory)
    text = "Como faço para anunciar um item?"
