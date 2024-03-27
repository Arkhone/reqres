import logging
from jsonschema import validate

import settings
from utils.requests import Client

logger = logging.getLogger("api")


class Post:
    def __init__(self, url):
        self.settings = settings
        self.url = url
        self.client = Client()

    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.settings.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info("A POST request recieved %s code", response.status_code)
        logger.info(response.text)
        return response

    def create_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.settings.POST_CREATE_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info("A POST request recieved %s code", response.status_code)
        logger.info(response.text)
        return response

    def login_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.settings.POST_LOGIN}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info("A POST request recieved %s code", response.status_code)
        logger.info(response.text)
        return response


class Get:
    def __init__(self, url):
        self.settings = settings
        self.url = url
        self.client = Client()

    def get(self, prefix: str):
        response = self.client.custom_request("GET", f"{self.url}{prefix}")
        logger.info(response.status_code)
        return response


