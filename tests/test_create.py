
import settings

from utils.api import Register
from utils.models import CreateUser
from schemas.registration import registration_schema

URL = settings.URL


def test_create_user():
    body = CreateUser.random_user_c()
    response = Register(url=URL).create_user(body=body, schema=registration_schema)
    print(response.json())
