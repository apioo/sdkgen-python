"""
ProductTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen

from test_request import TestRequest
from test_response import TestResponse

class ProductTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)
    pass


    """
    Returns a collection
    """
    def get_all(self, start_index: int, count: int, search: str) -> TestResponse:
        try:
            pathParams = {}

            queryParams = {}
            queryParams["startIndex"] = start_index
            queryParams["count"] = count
            queryParams["search"] = search

            url = self.parser.url("/anything", pathParams)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=queryParams)

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.from_json(response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    """
    Creates a new product
    """
    def create(self, payload: TestRequest) -> TestResponse:
        try:
            pathParams = {}

            queryParams = {}

            url = self.parser.url("/anything", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=queryParams, data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.from_json(response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    """
    Updates an existing product
    """
    def update(self, id: int, payload: TestRequest) -> TestResponse:
        try:
            pathParams = {}
            pathParams["id"] = id

            queryParams = {}

            url = self.parser.url("/anything/:id", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=queryParams, data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.from_json(response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    """
    Patches an existing product
    """
    def patch(self, id: int, payload: TestRequest) -> TestResponse:
        try:
            pathParams = {}
            pathParams["id"] = id

            queryParams = {}

            url = self.parser.url("/anything/:id", pathParams)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.patch(url, headers=headers, params=queryParams, data=payload.to_json())

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.from_json(response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass

    """
    Deletes an existing product
    """
    def delete(self, id: int) -> TestResponse:
        try:
            pathParams = {}
            pathParams["id"] = id

            queryParams = {}

            url = self.parser.url("/anything/:id", pathParams)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=queryParams)

            if response.status_code >= 200 and response.status_code < 300:
                return TestResponse.from_json(response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except Exception as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))
    pass


