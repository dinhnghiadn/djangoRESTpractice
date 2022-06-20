import pytest
from apps.subject.models import Subject


@pytest.mark.django_db
def test_create_subject_success(auth_client):
    payload = dict(
        name="Magical",
        term="2"
    )
    response = auth_client.post("/subject/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_subject_fail_validate_1(auth_client):
    payload = dict(
        term="2"
        # name field is required
    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_fail_validate_2(auth_client):
    payload = dict(
        name="Magical"
        # term field is required
    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_fail_validate_3(auth_client):
    payload = dict(
        name="",
        # blank field
        term="3"
    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_fail_validate_4(auth_client):
    payload = dict(
        name="Magical",

        term=""
        # blank field
    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_fail_validate_5(auth_client):
    payload = dict(
        name="Magicallllllllllllllllllllllllllllllllllllllllllllllllll",
        # max length is 50
        term="2"

    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_fail_validate_6(auth_client):
    payload = dict(
        name="Magical",
        term="3"
        # choices are 1 or 2 only
    )
    response = auth_client.post("/subject/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_subject_not_authentication(client):
    payload = dict(
        name="Magical",
        term="2"
    )
    response = client.post("/subject/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_subject_list_success(auth_client):
    Subject.objects.create(name="Magical", term="2")
    Subject.objects.create(name="Physical", term="1")
    response = auth_client.get("/subject/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_subject_success(auth_client, subject):
    response = auth_client.get(f"/subject/{subject.id}/")
    data = response.data
    assert data["name"] == subject.name
    assert data["term"] == subject.term


@pytest.mark.django_db
def test_get_subject_list_not_authentication(client):
    response = client.get("/subject/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_subject_not_authentication(client, subject):
    response = client.get(f"/subject/{subject.id}/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_subject_fail_404(auth_client):
    response = auth_client.get("/subject/0/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_subject_success(auth_client, subject):
    payload = dict(
        name="Physical",
        term="1"
    )
    response = auth_client.put(f"/subject/{subject.id}/", payload)
    subject.refresh_from_db()
    data = response.data
    assert data["name"] == subject.name
    assert data["term"] == subject.term


@pytest.mark.django_db
def test_update_subject_not_found(auth_client, subject):
    payload = dict(
        name="Physical",
        term="1"
    )
    wrong_id = "1000"
    response = auth_client.put(f"/subject/{wrong_id}/", payload)
    subject.refresh_from_db()
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_subject_not_authentication(client, subject):
    payload = dict(
        name="Physical",
        term="1"
    )
    response = client.put(f"/subject/{subject.id}/", payload)
    subject.refresh_from_db()
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_subject_success(auth_client, subject):
    response = auth_client.delete(f"/subject/{subject.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_subject_not_found(auth_client, subject):
    wrong_id = "1000"
    response = auth_client.put(f"/subject/{wrong_id}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_subject_not_authentication(client, subject):
    response = client.delete(f"/subject/{subject.id}/")
    assert response.status_code == 401
