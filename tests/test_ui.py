import pytest
import logging

from selenium.webdriver.common.by import By
from jsonschema import validate

import settings
import schemas.get as schema_get
import schemas.patch as schema_patch
import schemas.post as schema_post
from pages.main_page import MainPage


class TestGet:

    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.user = MainPage(driver)

    @pytest.fixture(params=[(settings.LIST_USERS_BUT, settings.GET_LIST_USERS, schema_get.list_users_schema,
                             settings.CODE_200),
                            (settings.SINGLE_USER_BUT, settings.GET_SINGLE_USER, schema_get.single_user_schema,
                             settings.CODE_200),
                            (settings.USER_NOT_FOUND_BUT, settings.GET_S_USER_NOT, schema_get.s_user_not_schema,
                             settings.CODE_404),
                            (settings.LIST_RES_BUT, settings.GET_LIST_RES, schema_get.list_res_schema,
                             settings.CODE_200),
                            (settings.SINGLE_RES_BUT, settings.GET_SINGLE_RES, schema_get.single_res_schema,
                             settings.CODE_200),
                            (settings.RES_NOT_FOUND_BUT, settings.GET_S_RES_NOT, schema_get.s_res_not_schema,
                             settings.CODE_404),
                            (settings.CREATE_BUT, settings.POST_CREATE_USER, schema_post.create_schema,
                             settings.CODE_201),
                            (settings.PUT_BUT, settings.PUT, schema_patch.put_update_schema,
                             settings.CODE_200),
                            (settings.PATCH_BUT, settings.PATCH, schema_patch.patch_update_schema,
                             settings.CODE_200),
                            (settings.DELETE_BUT, settings.DELETE, schema_patch.delete_schema,
                             settings.CODE_204),
                            (settings.REG_BUT, settings.POST_REGISTER_USER, schema_post.registration_schema,
                             settings.CODE_200),
                            (settings.REG_UNSUCCESS_BUT, settings.POST_REGISTER_USER,
                             schema_post.registration_unsucc_schema, settings.CODE_400),
                            (settings.LOGIN_BUT, settings.POST_LOGIN, schema_post.login_schema,
                             settings.CODE_200),
                            (settings.LOGIN_UNSUCCESS_BUT, settings.POST_LOGIN, schema_post.login_unsucc_schema,
                             settings.CODE_400),
                            (settings.DELAYED_BUT, settings.GET_DELAYED, schema_get.delayed_schema,
                             settings.CODE_200),
                            ])
    def get_data(self, request):
        return request.param

    def test_buttons(self, get_data):
        button_locator, prefix, schema, code = get_data
        code = str(code)
        self.user.click_on(button_locator, By.XPATH)
        self.user.wait_for_text(settings.RESPONSE_CODE, code, By.CLASS_NAME,)
        validate(instance=self.user.get_text(settings.OUTPUT_RESPONSE, By.XPATH), schema=schema)
        assert self.user.get_text(settings.PREFIX_URL, By.CSS_SELECTOR) == prefix
        assert self.user.get_text(settings.RESPONSE_CODE, By.CLASS_NAME) == code
        logging.info("A request with %s prefix, recieved %s code", prefix, code)

