"""
JsonException automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from src import sdkgen
from typing import Dict
from typing import Any


class JsonException(sdkgen.KnownStatusCodeException):
    payload: Any = None

    def __init__(self, payload):
        self.payload = payload

    def get_payload(self) -> Any:
        return self.payload
