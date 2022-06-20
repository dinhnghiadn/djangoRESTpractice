import pytest
from apps.classes.models import Class
from apps.teacher.models import Teacher


@pytest.mark.django_db
def test_create_teacher_success(auth_client, classes):
    payload = dict(
        name="Hans",
        gender="M",
        subject=classes.subject.id,
        classes=classes.id
    )

    response = auth_client.post("/teacher/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert data["gender"] == payload["gender"]
    assert data["subject"] == payload["subject"]
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_teacher_fail_validate_1(auth_client, classes):
    payload = dict(
        # name field is required
        gender="M",
        subject=classes.subject.id,
        classes=classes.id
    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_fail_validate_2(auth_client, classes):
    payload = dict(
        name="Hans",
        # gender field is required
        subject=classes.subject.id,
        classes=classes.id
    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_fail_validate_3(auth_client, classes):
    payload = dict(
        name="Hans",
        gender="M",
        # subject field is required
        classes=classes.id
    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_fail_validate_4(auth_client, classes):
    payload = dict(
        name="",
        gender="M",
        subject=classes.subject.id,
        classes=classes.id

    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_fail_validate_5(auth_client, classes):
    payload = dict(
        name="Hans",
        gender="G",
        # G not in choices
        subject=classes.subject.id,
        classes=classes.id

    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_fail_validate_6(auth_client, classes):
    payload = dict(
        name="Hans",
        gender="G",
        subject=classes.subject.id,
        classes=10000
        # class id not in database
    )
    response = auth_client.post("/teacher/", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_teacher_not_authentication(client, classes):
    payload = dict(
        name="Hans",
        gender="M",
        subject=classes.subject.id,
        classes=classes.id
    )
    response = client.post("/teacher/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_teacher_list_success(auth_client, classes):
    Teacher.objects.create(name="Hans", gender="M", subject=classes.subject, classes=classes)
    Teacher.objects.create(name="Solo", gender="M", subject=classes.subject, classes=classes)
    response = auth_client.get("/teacher/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_teacher_success(auth_client, teacher):
    response = auth_client.get(f"/teacher/{teacher.id}/")
    data = response.data
    assert data["name"] == teacher.name
    assert data["gender"] == teacher.gender


@pytest.mark.django_db
def test_get_teacher_list_not_authentication(client, classes):
    Teacher.objects.create(name="Hans", gender="M", subject=classes.subject, classes=classes)
    Teacher.objects.create(name="Solo", gender="M", subject=classes.subject, classes=classes)
    response = client.get("/teacher/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_class_not_authentication(client, teacher):
    response = client.get(f"/teacher/{teacher.id}/")
    data = response.data
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_teacher_fail_404(auth_client,teacher):
    response = auth_client.get("/teacher/0/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_teacher_success(auth_client, teacher):
    payload = dict(
        name="Solo",
        gender="F",
        subject=teacher.subject.id,
        classes= teacher.classes.id
    )

    response = auth_client.put(f"/teacher/{teacher.id}/", payload)
    teacher.refresh_from_db()
    data = response.data
    assert response.status_code == 200
    assert data["name"] == teacher.name


@pytest.mark.django_db
def test_update_teacher_not_found(auth_client, teacher):
    payload = dict(
        name="Solo",
        gender="F",
        subject=teacher.subject.id,
        classes=teacher.classes.id
    )

    wrong_id = "1000"
    response = auth_client.put(f"/class/{wrong_id}/", payload)
    teacher.refresh_from_db()
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_teacher_not_authentication(client, teacher):
    payload = dict(
        name="Solo",
        gender="F",
        subject=teacher.subject.id,
        classes=teacher.classes.id
    )
    response = client.put(f"/teacher/{teacher.id}/", payload)
    teacher.refresh_from_db()
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_teacher_success(auth_client, teacher):
    response = auth_client.delete(f"/teacher/{teacher.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_teacher_not_found(auth_client, teacher):
    wrong_id = "1000"
    response = auth_client.put(f"/teacher/{wrong_id}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_teacher_not_authentication(client, teacher):
    response = client.delete(f"/teacher/{teacher.id}/")
    assert response.status_code == 401
