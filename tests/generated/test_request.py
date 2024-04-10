"""
test_request automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List
from test_object import TestObject
from test_map_scalar import TestMapScalar
from test_map_object import TestMapObject
@dataclass_json
@dataclass
class TestRequest:
    int: int = field(default=None, metadata=config(field_name="int"))
    float: float = field(default=None, metadata=config(field_name="float"))
    string: str = field(default=None, metadata=config(field_name="string"))
    bool: bool = field(default=None, metadata=config(field_name="bool"))
    array_scalar: List[str] = field(default=None, metadata=config(field_name="arrayScalar"))
    array_object: List[TestObject] = field(default=None, metadata=config(field_name="arrayObject"))
    map_scalar: TestMapScalar = field(default=None, metadata=config(field_name="mapScalar"))
    map_object: TestMapObject = field(default=None, metadata=config(field_name="mapObject"))
    object: TestObject = field(default=None, metadata=config(field_name="object"))
