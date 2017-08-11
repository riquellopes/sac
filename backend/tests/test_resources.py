import json
import pytest
from .factories import (
    TypeCalledFactory, CountryFactory, ReasonFactory, RecordCalledFactory, )


@pytest.fixture
def types():
    TypeCalledFactory.create()
    TypeCalledFactory.create(type="chat")
    TypeCalledFactory.create(type="email")


@pytest.fixture
def countries():
    CountryFactory.create()
    CountryFactory.create(country="ES")


@pytest.fixture
def reasons():
    ReasonFactory.create()
    ReasonFactory.create(reason="elogios")
    ReasonFactory.create(reason="sugestões")


@pytest.fixture
def records_called():
    RecordCalledFactory.create_batch(5)


def test_service_type_called_should_return_a_list_of_types(test_client, types):
    response = test_client.get("/v1/type-called/")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))

    assert len(data.get("results")) == 3
    assert response.headers.get("Content-Type") == "application/json"


def test_service_countries_should_return_a_list_of_countries(test_client, countries):
    response = test_client.get("/v1/countries/")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))

    assert len(data.get("results")) == 2
    assert response.headers.get("Content-Type") == "application/json"


def test_service_reasons_should_return_a_list_of_reasons(test_client, reasons):
    response = test_client.get("/v1/reasons/")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))

    assert len(data.get("results")) == 3
    assert response.headers.get("Content-Type") == "application/json"


def test_(records_called):
    pass
