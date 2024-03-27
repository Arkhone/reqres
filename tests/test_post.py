import pytest

import settings as s
import schemas.post as sch

from jsonschema import validate
from utils.api import Post
from utils.models import RegisterUser as Ru


@pytest.fixture(params=[(s.POST_CREATE_USER, s.CODE_201, sch.create_schema, Ru.random_user_c()),
                        (s.POST_REGISTER_USER, s.CODE_200, sch.registration_schema, Ru.registration_user())
                        ])
def post_data(request):
    return request.param


def test_create(post_data):
    prefix, kod, schema, body = post_data
    response = Post(url=s.URL).post(prefix=prefix, body=body)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == kod
    assert response.json().get('id')


@pytest.fixture(params=[(s.POST_LOGIN, s.CODE_200, sch.login_schema, Ru.login_user()),
                        (s.POST_REGISTER_USER, s.CODE_400, sch.registration_unsucc_schema, Ru.invalid_user()),
                        (s.POST_REGISTER_USER, s.CODE_400, sch.login_unsucc_schema, Ru.invalid_user())
                        ])
def login_data(request):
    return request.param


def test_login(login_data):
    prefix, kod, schema, body = login_data
    response = Post(url=s.URL).post(prefix=prefix, body=body)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == kod
