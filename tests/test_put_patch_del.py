import pytest

import settings
import schemas.patch as schemas
from utils.api import Patch
from utils.models import UpdateUser


def test_patch():
    body = UpdateUser.user_up()
    response = Patch(url=settings.URL).patch(body=body, schema=schemas.patch_update_schema)
    assert response.status_code == 200


def test_put():
    body = UpdateUser.user_up()
    response = Patch(url=settings.URL).put(body=body, schema=schemas.patch_update_schema)
    assert response.status_code == 200


def test_delete():
    response = Patch(url=settings.URL).delete()
    assert response.status_code == 204
