import pytest

from jsonschema import validate

import settings
import schemas.get as schemas
from utils.api import Get


@pytest.fixture(params=[(Get(url=settings.URL).get(settings.GET_SINGLE_USER), schemas.single_user_schema,
                         settings.CODE_200),
                        (Get(url=settings.URL).get(settings.GET_LIST_USERS), schemas.list_users_schema,
                         settings.CODE_200),
                        (Get(url=settings.URL).get(settings.GET_SINGLE_RES), schemas.single_res_schema,
                         settings.CODE_200),
                        (Get(url=settings.URL).get(settings.GET_LIST_RES), schemas.list_res_schema,
                         settings.CODE_200),
                        (Get(url=settings.URL).get(settings.GET_DELAYED), schemas.delayed_schema,
                         settings.CODE_200),
                        (Get(url=settings.URL).get(settings.GET_S_USER_NOT), schemas.s_res_not_schema,
                         settings.CODE_404),
                        (Get(url=settings.URL).get(settings.GET_S_RES_NOT), schemas.s_res_not_schema,
                         settings.CODE_404)
                        ])
def get_data(request):
    return request.param


def test_get(get_data):
    resp, schema, code = get_data
    response = resp
    validate(instance=response.json(), schema=schema)
    assert response.status_code == code



