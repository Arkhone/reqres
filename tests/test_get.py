import pytest

from jsonschema import validate

import settings as s
import schemas.get as sch
from utils.api import Get


@pytest.fixture(params=[(s.GET_SINGLE_USER, sch.single_user_schema, s.CODE_200),
                        (s.GET_LIST_USERS, sch.list_users_schema, s.CODE_200),
                        (s.GET_SINGLE_RES, sch.single_res_schema, s.CODE_200),
                        (s.GET_LIST_RES, sch.list_res_schema, s.CODE_200),
                        (s.GET_DELAYED, sch.delayed_schema, s.CODE_200),
                        (s.GET_S_USER_NOT, sch.s_res_not_schema, s.CODE_404),
                        (s.GET_S_RES_NOT, sch.s_res_not_schema, s.CODE_404)
                        ])
def get_data(request):
    return request.param


def test_get(get_data):
    prefix, schema, code = get_data
    response = Get(url=s.URL).get(prefix)
    validate(instance=response.json(), schema=schema)
    assert response.status_code == code



