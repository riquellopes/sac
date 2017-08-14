import json
from .factories import TypeCalledFactory, CountryFactory, ReasonFactory


def test_service_should_response_201_when_saved(test_client):

    data = {
        "text": "Meu anuncio está sendo bloqueado.",
        "type_called_id": TypeCalledFactory.create().id,
        "country_id": CountryFactory.create().id,
        "reason_id": ReasonFactory.create().id
    }

    response = test_client.post(
        "/v1/recordcalled/",
        data=json.dumps(data),
        content_type='application/json')

    assert response.status_code == 201


def test_service_should_response_422_when_unprocess(test_client):
    response = test_client.post(
        "/v1/recordcalled/",
        data=json.dumps({}),
        content_type='application/json')

    assert response.status_code == 422


def test_should_get_error_when_json_content_type_undefined(test_client):
    data = {
        "text": "Meu anuncio está sendo bloqueado.",
        "type_called_id": TypeCalledFactory.create().id,
        "country_id": CountryFactory.create().id,
        "reason_id": ReasonFactory.create().id
    }

    response = test_client.post(
        "/v1/recordcalled/",
        data=json.dumps(data))

    assert response.status_code == 422

    data = json.loads(response.data.decode('utf-8'))
    assert data['messages']['text'][0] == "Missing data for required field."
