# coding: utf-8
from .factories import TypeCalledFactory, CountryFactory, ReasonFactory
from app.models import RecordCalled
from app.api import db


def test_should_created_id_when_save_successfully():
    record = RecordCalled(
        type=TypeCalledFactory.create(),
        country=CountryFactory.create(),
        reason=ReasonFactory.create(),
        text="Serviço nota 10."
    )

    db.session.add(record)
    db.session.commit()

    assert record.id
    assert record.text == "Serviço nota 10."
