import pytest

import settings
import schemas.get as schemas
from utils.api import Get


@pytest.fixture(params=[Get(url=settings.URL).get(settings.GET_SINGLE_USER, schema=schemas.single_user_schema),
                        Get(url=settings.URL).get(settings.GET_LIST_USERS, schema=schemas.list_users_schema),
                        Get(url=settings.URL).get(settings.GET_SINGLE_RES, schema=schemas.single_res_schema),
                        Get(url=settings.URL).get(settings.GET_LIST_RES, schema=schemas.list_res_schema),
                        Get(url=settings.URL).get(settings.GET_DELAYED, schema=schemas.delayed_schema)
                        ])
def get_200(request):
    return request.param


@pytest.fixture(params=[Get(url=settings.URL).get(settings.GET_S_USER_NOT, schema=schemas.s_res_not_schema),
                        Get(url=settings.URL).get(settings.GET_S_RES_NOT, schema=schemas.s_res_not_schema),
                        ])
def get_404(request):
    return request.param


def test_get_200(get_200):
    response = get_200
    assert response.status_code == 200


def test_get_404(get_404):
    response = get_404
    assert response.status_code == 404
