import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to my Flask app" in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"This is the about page" in response.data

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact us" in response.data

def test_invalid_page(client):
    response = client.get('/invalid')
    assert response.status_code == 404
