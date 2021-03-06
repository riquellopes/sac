import json
import pytest
from .factories import TypeCalledFactory, CountryFactory, ReasonFactory, RecordCalledFactory


@pytest.fixture
def types():
    TypeCalledFactory.create_batch(3)


@pytest.fixture
def countries():
    CountryFactory.create_batch(2)


@pytest.fixture
def reasons():
    ReasonFactory.create_batch(3)


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


def test_service_record_should_return_a_list_of_records(test_client, records_called):
    response = test_client.get("/v1/recordcalled/")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))

    assert len(data.get("results")) == 5
    assert response.headers.get("Content-Type") == "application/json"


def test_should_get_a_empty_result_list_when_no_data_recorded(test_client):
    response = test_client.get("/v1/recordcalled/")

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))

    assert len(data.get("results")) == 0
    assert response.headers.get("Content-Type") == "application/json"
