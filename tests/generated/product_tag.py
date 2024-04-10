"""
ProductTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
from requests import RequestException
from typing import List

from src import sdkgen
from .test_request import TestRequest
from .test_response import TestResponse

class ProductTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, start_index: int, count: int, search: str) -> TestResponse:
        """
        Returns a collection
        """
        try:
            path_params = {}

            query_params = {}
            query_params["startIndex"] = start_index
            query_params["count"] = count
            query_params["search"] = search

            query_struct_names = []

            url = self.parser.url("/anything", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create(self, payload: TestRequest) -> TestResponse:
        """
        Creates a new product
        """
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/anything", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update(self, id: int, payload: TestRequest) -> TestResponse:
        """
        Updates an existing product
        """
        try:
            path_params = {}
            path_params["id"] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/anything/:id", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def patch(self, id: int, payload: TestRequest) -> TestResponse:
        """
        Patches an existing product
        """
        try:
            path_params = {}
            path_params["id"] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/anything/:id", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.patch(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def delete(self, id: int) -> TestResponse:
        """
        Deletes an existing product
        """
        try:
            path_params = {}
            path_params["id"] = id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/anything/:id", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


