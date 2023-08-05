import settings
import schemas.post as schemas

from utils.api import Post
from utils.models import RegisterUser


def test_create():
    body = RegisterUser.random_user_c()
    response = Post(url=settings.URL).create_user(body=body, schema=schemas.create_schema)
    assert response.status_code == 201
    assert response.json().get('id')


def test_registration():
    body = RegisterUser.registration_user()
    response = Post(url=settings.URL).register_user(body=body, schema=schemas.registration_schema)
    assert response.status_code == 200
    assert response.json().get('id')


def test_login():
    body = RegisterUser.login_user()
    response = Post(url=settings.URL).login_user(body=body, schema=schemas.login_schema)
    assert response.status_code == 200


def test_registration_unsuccess():
    body = RegisterUser.invalid_user()
    response = Post(url=settings.URL).register_user(body=body, schema=schemas.registration_unsucc_schema)
    assert response.status_code == 400


def test_login_unsuccess():
    body = RegisterUser.invalid_user()
    response = Post(url=settings.URL).login_user(body=body, schema=schemas.login_unsucc_schema)
    assert response.status_code == 400
