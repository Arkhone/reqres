# URL's

URL = "https://reqres.in"
# Prefix

PUT = '/api/users/2'
PATCH = '/api/users/2'
DELETE = '/api/users/2'

POST_REGISTER_USER = '/api/register'
POST_CREATE_USER = '/api/users'
POST_LOGIN = '/api/login'


GET_SINGLE_USER = '/api/users/2'
GET_LIST_USERS = '/api/users?page=2'
GET_S_USER_NOT = '/api/users/23'
GET_LIST_RES = '/api/unknown'
GET_SINGLE_RES = '/api/unknown/2'
GET_S_RES_NOT = '/api/unknown/23'
GET_DELAYED = '/api/users?delay=3'

# Status_code
CODE_200 = 200
CODE_201 = 201
CODE_204 = 204
CODE_400 = 400
CODE_404 = 404

# Locators
# Button locators

LIST_USERS_BUT = "//section[@id='console']//ul/li[1]"
SINGLE_USER_BUT = "//section[@id='console']//ul/li[2]"
USER_NOT_FOUND_BUT = "//section[@id='console']//ul/li[3]"
LIST_RES_BUT = "//section[@id='console']//ul/li[4]"
SINGLE_RES_BUT = "//section[@id='console']//ul/li[5]"
RES_NOT_FOUND_BUT = "//section[@id='console']//ul/li[6]"
CREATE_BUT = "//section[@id='console']//ul/li[7]"
PUT_BUT = "//section[@id='console']//ul/li[8]"
PATCH_BUT = "//section[@id='console']//ul/li[9]"
DELETE_BUT = "//section[@id='console']//ul/li[10]"
REG_BUT = "//section[@id='console']//ul/li[11]"
REG_UNSUCCESS_BUT = "//section[@id='console']//ul/li[12]"
LOGIN_BUT = "//section[@id='console']//ul/li[13]"
LOGIN_UNSUCCESS_BUT = "//section[@id='console']//ul/li[14]"
DELAYED_BUT = "//section[@id='console']//ul/li[15]"


# Field locators

PREFIX_URL = ".link.try-link > .url"
RESPONSE_CODE = "response-code"
OUTPUT_RESPONSE = "//div[@class='response']/pre"