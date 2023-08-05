import settings
from utils.api import Register
from utils.models import CreateUser
from utils.models import RegisterUser
from schemas.registration import create_schema
from schemas.registration import registration_schema


URL = settings.URL


def test_create_pos():
    body = CreateUser.random_user_c()
    response = Register(url=URL).create_user(body=body, schema=create_schema)
    assert response.status_code == 201
    assert response.json().get('id')


def test_registration_pos():
    body = RegisterUser.random_user_r()
    response = Register(url=URL).register_user(body=body, schema=registration_schema)
    assert response.status_code == 200
    assert response.json().get('id')
