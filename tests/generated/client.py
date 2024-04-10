"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
from requests import RequestException
from typing import List

from src import sdkgen
from .product_tag import ProductTag

class Client(sdkgen.ClientAbstract):
    @classmethod
    def __init__(cls, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)

    @classmethod
    def product(cls) -> ProductTag:
        return ProductTag(
            cls.http_client,
            cls.parser
        )



    @staticmethod
    def build(token: str):
        return Client("http://127.0.0.1:8081", sdkgen.HttpBearer(token))

