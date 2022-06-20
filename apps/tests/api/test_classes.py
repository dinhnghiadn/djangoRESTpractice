import pytest
from apps.classes.models import Class


@pytest.mark.django_db
def test_create_class_success(auth_client, subject):
    payload = dict(
        name="F101",
        date_create="2022-05-05",
        subject=subject.id
    )

    response = auth_client.post("/class/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert data["date_create"] == payload["date_create"]
    assert data["subject"] == payload["subject"]
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_class_fail_validate_1(auth_client, subject):
    payload = dict(
        # name field is required
        date_create="2022-05-05",
        subject=subject.id
    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_fail_validate_2(auth_client, subject):
    payload = dict(
        name="Magical",
        # date_create field is required
        subject=subject.id
    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_fail_validate_3(auth_client, subject):
    payload = dict(
        name="H101",
        date_create="2022-05-05",
        # subject field is required
    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_fail_validate_4(auth_client, subject):
    payload = dict(
        name="",
        # blank field
        date_create="2022-05-05",
        subject=subject.id

    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_fail_validate_5(auth_client, subject):
    payload = dict(
        name="B50501",
        # max length is 5
        date_create="2022-05-05",
        subject=subject.id

    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_fail_validate_6(auth_client, subject):
    payload = dict(
        name="H101",
        date_create="2022-05-05",
        subject=1000
        # subject id is not in db
    )
    response = auth_client.post("/class/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_class_not_authentication(client, subject):
    payload = dict(
        name="H101",
        date_create="2022-05-05",
        subject=subject.id
    )
    response = client.post("/class/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_class_list_success(auth_client, subject):
    Class.objects.create(name="A909", date_create="2022-03-03", subject=subject)
    Class.objects.create(name="B606", date_create="2022-04-04", subject=subject)
    response = auth_client.get("/class/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_class_success(auth_client, classes):
    response = auth_client.get(f"/class/{classes.id}/")
    data = response.data
    assert data["name"] == classes.name
    assert data["date_create"] == classes.date_create


@pytest.mark.django_db
def test_get_class_list_not_authentication(client, subject):
    Class.objects.create(name="A909", date_create="2022-03-03", subject=subject)
    Class.objects.create(name="B606", date_create="2022-04-04", subject=subject)
    response = client.get("/class/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_class_not_authentication(client, classes):
    response = client.get(f"/class/{classes.id}/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_class_fail_404(auth_client,classes):
    response = auth_client.get("/class/0/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_class_success(auth_client, classes):
    payload = dict(
        name="E505",
        date_create="2021-01-01",
        subject=classes.subject.id
    )

    response = auth_client.put(f"/class/{classes.id}/", payload)
    classes.refresh_from_db()
    data = response.data
    assert response.status_code == 200
    assert data["name"] == classes.name


@pytest.mark.django_db
def test_update_class_not_found(auth_client, classes):
    payload = dict(
        name="E505",
        date_create="2021-01-01",
        subject=classes.subject.id
    )
    wrong_id = "1000"
    response = auth_client.put(f"/class/{wrong_id}/", payload)
    classes.refresh_from_db()
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_class_not_authentication(client, classes):
    payload = dict(
        name="E505",
        date_create="2021-12-12",
        subject=classes.subject.id
    )
    response = client.put(f"/class/{classes.id}/", payload)
    classes.refresh_from_db()
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_class_success(auth_client, classes):
    response = auth_client.delete(f"/class/{classes.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_class_not_found(auth_client, classes):
    wrong_id = "1000"
    response = auth_client.put(f"/classes/{wrong_id}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_class_not_authentication(client, classes):
    response = client.delete(f"/class/{classes.id}/")
    assert response.status_code == 401
