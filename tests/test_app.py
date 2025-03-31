from fastapi import status
from fastapi.testclient import TestClient

from ignor.app import app

client = TestClient(app)


def test_root():
    """
    Test the root endpoint
    """
    response = client.get('/api/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'Developed by @machadoah and @isaahs 🤓'
    }


def test_list_templates():
    """
    Test the list templates endpoint
    """
    response = client.get('/api/templates/list')
    assert response.status_code == status.HTTP_200_OK
    assert 'templates' in response.json()
    assert isinstance(response.json()['templates'], list)


def test_verify_template():
    """
    Test the verify template endpoint
    """
    response = client.get('/api/templates/verify/test_template')
    assert response.status_code == status.HTTP_200_OK
    assert 'templates' in response.json()
    assert isinstance(response.json()['templates'], list)


def test_redirect_to_docs():
    """
    Test the redirect to docs endpoint
    """

    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
