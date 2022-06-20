import pytest

from apps.user.models import User


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        email="nghia500@gmail.com",
        password="12345"
    )
    response = client.post("/register", payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_register_user_existing_email(client):
    User.objects.create(email="nghia500@gmail.com", password="123")
    payload = dict(
        email="nghia500@gmail.com",
        password="12345"
    )
    response = client.post("/register", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user(client):
    payload = dict(
        email="nghia500@gmail.com",
        password="12345"
    )
    client.post("/register", payload)
    response = client.post("/login", dict(email="nghia500@gmail.com", password="12345"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post("/login", dict(email="nghia500@gmail.com", password="123"))
    assert response.status_code == 401
