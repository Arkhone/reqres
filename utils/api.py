import logging

import settings
from utils.requests import Client

logger = logging.getLogger("api")


class Post:
    def __init__(self, url):
        self.settings = settings
        self.url = url
        self.client = Client()

    def post(self, prefix: str, body: dict):
        response = self.client.custom_request("POST", f"{self.url}{prefix}", json=body)
        logger.info(prefix)
        logger.info("A POST request recieved %s code", response.status_code)
        return response


class Get:
    def __init__(self, url):
        self.settings = settings
        self.url = url
        self.client = Client()

    def get(self, prefix: str):
        response = self.client.custom_request("GET", f"{self.url}{prefix}")
        logger.info(prefix)
        return response


class Patch:
    def __init__(self, url):
        self.settings = settings
        self.url = url
        self.client = Client()

    def patch(self, prefix: str, body: dict):
        response = self.client.custom_request("PATCH", f"{self.url}{prefix}", json=body)
        logger.info("A PATCH request recieved %s code", response.status_code)
        return response

    def put(self, prefix: str, body: dict):
        response = self.client.custom_request("PUT", f"{self.url}{prefix}", json=body)
        logger.info("A PUT request recieved %s code", response.status_code)
        return response

    def delete(self, prefix: str):
        response = self.client.custom_request("DELETE", f"{self.url}{prefix}")
        logger.info("A DELETE request recieved %s code", response.status_code)
        return response
