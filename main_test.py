import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/infoUser/Chyna42')
    assert response.status_code == 200