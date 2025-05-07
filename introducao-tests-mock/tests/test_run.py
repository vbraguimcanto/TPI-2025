import pytest
from unittest import mock
from my_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data_success(client):
    with mock.patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {'id': 1, 'title': 'Test Post'}

        response = client.get('/get_data')

        assert response.status_code == 200
        assert response.get_json() == {'id': 1, 'title': 'Test Post'}

def test_get_data_failure(client):
    with mock.patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 500
        mocked_get.return_value.json.return_value = {'error': 'Failed to fetch data'}

        response = client.get('/get_data')

        assert response.status_code == 500
        assert response.get_json() == {'error': 'Failed to fetch data'}