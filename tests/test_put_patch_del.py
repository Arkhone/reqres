import settings as s
import schemas.patch as sch

from jsonschema import validate
from utils.api import Patch
from utils.models import UpdateUser


def test_patch():
    body = UpdateUser.user_up()
    response = Patch(url=s.URL).patch(s.PATCH, body=body)
    validate(instance=response.json(), schema=sch.patch_update_schema)
    assert response.status_code == s.CODE_200


def test_put():
    body = UpdateUser.user_up()
    response = Patch(url=s.URL).put(s.PUT, body=body)
    validate(instance=response.json(), schema=sch.patch_update_schema)
    assert response.status_code == s.CODE_200


def test_delete():
    response = Patch(url=s.URL).delete(s.DELETE)
    assert response.status_code == s.CODE_204
