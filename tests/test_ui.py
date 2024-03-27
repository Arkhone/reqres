import pytest
import logging

from selenium.webdriver.common.by import By
from jsonschema import validate

import settings as s
import schemas.get as sch_get
import schemas.patch as sch_patch
import schemas.post as sch_post
from pages.main_page import MainPage


class TestGet:

    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.user = MainPage(driver)

    @pytest.fixture(params=[(s.LIST_USERS_BUT, s.GET_LIST_USERS, sch_get.list_users_schema, s.CODE_200),
                            (s.SINGLE_USER_BUT, s.GET_SINGLE_USER, sch_get.single_user_schema, s.CODE_200),
                            (s.USER_NOT_FOUND_BUT, s.GET_S_USER_NOT, sch_get.s_user_not_schema, s.CODE_404),
                            (s.LIST_RES_BUT, s.GET_LIST_RES, sch_get.list_res_schema, s.CODE_200),
                            (s.SINGLE_RES_BUT, s.GET_SINGLE_RES, sch_get.single_res_schema, s.CODE_200),
                            (s.RES_NOT_FOUND_BUT, s.GET_S_RES_NOT, sch_get.s_res_not_schema, s.CODE_404),
                            (s.CREATE_BUT, s.POST_CREATE_USER, sch_post.create_schema, s.CODE_201),
                            (s.PUT_BUT, s.PUT, sch_patch.put_update_schema, s.CODE_200),
                            (s.PATCH_BUT, s.PATCH, sch_patch.patch_update_schema, s.CODE_200),
                            (s.DELETE_BUT, s.DELETE, sch_patch.delete_schema, s.CODE_204),
                            (s.REG_BUT, s.POST_REGISTER_USER, sch_post.reg_schema, s.CODE_200),
                            (s.REG_UNSUCCESS_BUT, s.POST_REGISTER_USER, sch_post.reg_unsuccess_schema, s.CODE_400),
                            (s.LOGIN_BUT, s.POST_LOGIN, sch_post.login_schema, s.CODE_200),
                            (s.LOGIN_UNSUCCESS_BUT, s.POST_LOGIN, sch_post.login_unsucc_schema, s.CODE_400),
                            (s.DELAYED_BUT, s.GET_DELAYED, sch_get.delayed_schema, s.CODE_200),
                            ])
    def get_data(self, request):
        return request.param

    def test_buttons(self, get_data):
        button_locator, prefix, schema, code = get_data
        code = str(code)
        self.user.click_on(button_locator, By.XPATH)
        self.user.wait_for_text(s.RESPONSE_CODE, code, By.CLASS_NAME,)
        validate(instance=self.user.get_text(s.OUTPUT_RESPONSE, By.XPATH), schema=schema)
        assert self.user.get_text(s.PREFIX_URL, By.CSS_SELECTOR) == prefix
        assert self.user.get_text(s.RESPONSE_CODE, By.CLASS_NAME) == code
        logging.info("A request with %s prefix, recieved %s code", prefix, code)

