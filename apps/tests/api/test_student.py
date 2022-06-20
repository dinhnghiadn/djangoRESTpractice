import pytest
from apps.student.models import Student


@pytest.mark.django_db
def test_create_student_success(auth_client, classes):
    payload = {
        "name": "Jack",
        "date_of_birth": "1992-05-10",
        "gender": "M",
        "email": "jack2@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    data = response.data
    assert response.status_code == 201
    assert data["name"] == payload["name"]
    assert data["date_of_birth"] == payload["date_of_birth"]
    assert data["gender"] == payload["gender"]


@pytest.mark.django_db
def test_create_student_fail_validate_1(auth_client, classes):
    payload = {
        # name field is required
        "date_of_birth": "1992-05-10",
        "gender": "M",
        "email": "jack2@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_student_fail_validate_2(auth_client, classes):
    payload = {
        "name": "Jack",
        # date_of_birth field is required
        "gender": "M",
        "email": "jack2@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_student_fail_validate_4(auth_client, classes):
    payload = {
        "name": "Jack",
        "date_of_birth": "1992-05-10",
        # gender field is required
        "email": "jack2@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_student_fail_validate_5(auth_client, classes):
    payload = {
        "name": "Jack",
        "date_of_birth": "1992-05-10",
        "gender": "M",
        # email field is required
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_student_fail_validate_6(auth_client, classes):
    payload = {
        "name": "Jack",
        "date_of_birth": "1992-05-10",
        "gender": "M",
        "email": "jacky@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": 10000
                # subject not in database
            }
        ]
    }
    response = auth_client.post("/student/", payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_student_not_authentication(client, classes):
    payload = {
        "name": "Jack",
        "date_of_birth": "1992-05-10",
        "gender": "M",
        "email": "jack2@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": classes.name,
                "date_create": classes.date_create,
                "subject": classes.subject.id
            }
        ]
    }
    response = client.post("/student/", payload, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_student_list_success(auth_client, classes):
    student_1 = Student.objects.create(name="Jim", date_of_birth="1992-05-05", gender="M", email="jim@gmail.com",
                                       address="New York")

    student_2 = Student.objects.create(name="Bil", date_of_birth="1993-05-05", gender="M", email="bil@gmail.com",
                                       address="New York")
    student_1.classes.add(classes)
    student_2.classes.add(classes)
    response = auth_client.get("/student/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_student_success(auth_client, student):
    response = auth_client.get(f"/student/{student.id}/")
    data = response.data
    assert data["name"] == student.name
    assert data["date_of_birth"] == student.date_of_birth


@pytest.mark.django_db
def test_get_student_list_success_not_authentication(client, classes):
    student_1 = Student.objects.create(name="Jim", date_of_birth="1992-05-05", gender="M", email="jim@gmail.com",
                                       address="New York")

    student_2 = Student.objects.create(name="Bil", date_of_birth="1993-05-05", gender="M", email="bil@gmail.com",
                                       address="New York")
    student_1.classes.add(classes)
    student_2.classes.add(classes)
    response = client.get("/student/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_student_not_authentication(client, student):
    response = client.get(f"/student/{student.id}/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_student_fail_404(auth_client, student):
    response = auth_client.get("/student/0/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_student_success(auth_client, student):
    class_data = student.classes.all().first()
    print(f'{class_data}')
    payload = {
        "name": "Dan",
        "date_of_birth": "1993-05-10",
        "gender": "M",
        "email": "danny@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": class_data.name,
                "date_create": class_data.date_create,
                "subject": class_data.subject.id
            }
        ]
    }
    response = auth_client.put(f"/student/{student.id}/", payload, format="json")
    data = response.data
    assert response.status_code == 200
    assert data["name"] == payload["name"]
    assert data["date_of_birth"] == payload["date_of_birth"]
    assert data["email"] == payload["email"]


@pytest.mark.django_db
def test_update_student_not_found(auth_client, student):
    class_data = student.classes.all().first()
    print(f'{class_data}')
    payload = {
        "name": "Dan",
        "date_of_birth": "1993-05-10",
        "gender": "M",
        "email": "danny@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": class_data.name,
                "date_create": class_data.date_create,
                "subject": class_data.subject.id
            }
        ]
    }
    wrong_id = 1000
    response = auth_client.put(f"/student/{wrong_id}/", payload, format="json")
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_student_not_authentication(client, student):
    class_data = student.classes.all().first()
    print(f'{class_data}')
    payload = {
        "name": "Dan",
        "date_of_birth": "1993-05-10",
        "gender": "M",
        "email": "danny@gmail.com",
        "address": "Texas",
        "classes": [
            {
                "name": class_data.name,
                "date_create": class_data.date_create,
                "subject": class_data.subject.id
            }
        ]
    }

    response = client.put(f"/student/{student.id}/", payload, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_student_success(auth_client, student):
    response = auth_client.delete(f"/student/{student.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_student_not_found(auth_client, student):
    wrong_id = "1000"
    response = auth_client.put(f"/student/{wrong_id}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_student_not_authentication(client, student):
    response = client.delete(f"/student/{student.id}/")
    assert response.status_code == 401
