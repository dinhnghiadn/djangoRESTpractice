import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.classes.models import Class
from apps.student.models import Student
from apps.subject.models import Subject
from apps.teacher.models import Teacher
from apps.user.models import User


@pytest.fixture
def user():
    user = User.objects.create_user(email="nghiagbf500@gmail.com", password="12345")
    return user


@pytest.fixture
def subject():
    subject = Subject.objects.create(name="Magical", term="2")
    return subject


@pytest.fixture
def classes(subject):
    classes = Class.objects.create(name="H101", date_create="2022-03-03", subject=subject)
    return classes


@pytest.fixture
def student(classes):
    student = Student.objects.create(name="Jim", date_of_birth="1992-05-05", gender="M", email="jim@gmail.com",
                                     address="New York")
    student.classes.add(classes)
    return student

@pytest.fixture
def teacher(classes):
    teacher = Teacher.objects.create(name="Hans", gender="M", subject=classes.subject, classes=classes)
    return teacher


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(user, client):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client
