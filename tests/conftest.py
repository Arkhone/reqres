import pytest

import settings

from utils.api import Post
from utils.models import RegisterUser
from schemas.post import registration_schema

URL = settings.URL


@pytest.fixture()
def create_user():
    body = RegisterUser.random_user_c()
    response = Post(url=URL).register_user(body=body, schema=registration_schema)
    return response.json()
