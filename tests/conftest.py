import pytest

import settings

from utils.api import Register
from utils.models import CreateUser
from schemas.registration import registration_schema

URL = settings.URL


@pytest.fixture()
def create_user():
    body = CreateUser.random_user_c()
    response = Register(url=URL).register_user(body=body, schema=registration_schema)
    return response.json()
