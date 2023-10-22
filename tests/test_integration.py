import unittest
from .generated.client import Client
from .generated.test_request import TestRequest
from .generated.test_object import TestObject


class TestIntegration(unittest.TestCase):
    def test_client_get_all(self):
        client = Client.build("my_token")

        response = client.product().get_all(8, 16, "foobar")

        self.assertEqual(response.headers["Authorization"], "Bearer my_token")
        self.assertEqual(response.headers["Accept"], "application/json")
        self.assertEqual(response.headers["User-Agent"], "SDKgen Client v1.0")
        self.assertEqual(response.method, "GET")
        self.assertEqual(response.args["startIndex"], "8")
        self.assertEqual(response.args["count"], "16")
        self.assertEqual(response.args["search"], "foobar")
        self.assertEqual(response.json,
                         "{\"int\":0,\"float\":0,\"string\":\"\",\"bool\":false,\"arrayScalar\":null,\"arrayObject\":null,\"mapScalar\":null,\"mapObject\":null,\"object\":{\"id\":0,\"name\":\"\"}}")

    def test_client_create(self):
        client = Client.build("my_token")

        payload = self.new_payload()
        response = client.product().create(payload)

        self.assertEqual(response.headers["Authorization"], "Bearer my_token")
        self.assertEqual(response.headers["Accept"], "application/json")
        self.assertEqual(response.headers["User-Agent"], "SDKgen Client v1.0")
        self.assertEqual(response.method, "POST")
        self.assertEqual(response.json,
                         "{\"int\":0,\"float\":0,\"string\":\"\",\"bool\":false,\"arrayScalar\":null,\"arrayObject\":null,\"mapScalar\":null,\"mapObject\":null,\"object\":{\"id\":0,\"name\":\"\"}}")

    def test_client_update(self):
        client = Client.build("my_token")

        payload = self.new_payload()
        response = client.product().update(1, payload)

        self.assertEqual(response.headers["Authorization"], "Bearer my_token")
        self.assertEqual(response.headers["Accept"], "application/json")
        self.assertEqual(response.headers["User-Agent"], "SDKgen Client v1.0")
        self.assertEqual(response.method, "PUT")
        self.assertEqual(response.json,
                         "{\"int\":0,\"float\":0,\"string\":\"\",\"bool\":false,\"arrayScalar\":null,\"arrayObject\":null,\"mapScalar\":null,\"mapObject\":null,\"object\":{\"id\":0,\"name\":\"\"}}")

    def test_client_patch(self):
        client = Client.build("my_token")

        payload = self.new_payload()
        response = client.product().patch(1, payload)

        self.assertEqual(response.headers["Authorization"], "Bearer my_token")
        self.assertEqual(response.headers["Accept"], "application/json")
        self.assertEqual(response.headers["User-Agent"], "SDKgen Client v1.0")
        self.assertEqual(response.method, "PATCH")
        self.assertEqual(response.json,
                         "{\"int\":0,\"float\":0,\"string\":\"\",\"bool\":false,\"arrayScalar\":null,\"arrayObject\":null,\"mapScalar\":null,\"mapObject\":null,\"object\":{\"id\":0,\"name\":\"\"}}")

    def test_client_delete(self):
        client = Client.build("my_token")

        response = client.product().delete(1)

        self.assertEqual(response.headers["Authorization"], "Bearer my_token")
        self.assertEqual(response.headers["Accept"], "application/json")
        self.assertEqual(response.headers["User-Agent"], "SDKgen Client v1.0")
        self.assertEqual(response.method, "DELETE")
        self.assertEqual(response.json,
                         "{\"int\":0,\"float\":0,\"string\":\"\",\"bool\":false,\"arrayScalar\":null,\"arrayObject\":null,\"mapScalar\":null,\"mapObject\":null,\"object\":{\"id\":0,\"name\":\"\"}}")

    def new_payload(self) -> TestRequest:
        object_foo = TestObject(1, "foo")
        object_bar = TestObject(1, "bar")

        array_scalar = ["foo", "bar"]
        array_object = [object_foo, object_bar]

        map_scalar = {"foo": "bar", "bar": "foo"}
        map_object = {"foo": object_foo, "bar": object_bar}

        return TestRequest(1337, 13.37, "foobar", True, array_scalar, array_object, map_scalar, map_object, object_foo)


if __name__ == '__main__':
    unittest.main()
