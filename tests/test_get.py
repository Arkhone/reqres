import pytest

import settings
from utils.api import Get
from schemas.get import single_user_schema
from schemas.get import list_users_schema
from settings import GET_LIST_USERS
URL = settings.URL


@pytest.mark.parametrize("pref, schema_type, code", [
    ("/api/users/2", "single_user_schema", 200),
    ("/api/users?page=2", "list_users_schema", 200),
])
def test_get(pref, schema_type, code):
    response = Get(url=URL).get(pref, schema=schema_type)
    assert response.status_code == code

# def test_get_list_users():
# response = Get(url=URL).get(settings.GET_LIST_USERS, schema=list_users_schema)
# assert response.status_code == 200
