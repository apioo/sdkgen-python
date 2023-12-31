"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import sdkgen

from product_tag import ProductTag

class Client(sdkgen.ClientAbstract):
    def __init__(self, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)
    pass

    def product(self) -> ProductTag:
        return ProductTag(
            self.http_client,
            self.parser
        )
    pass



    @staticmethod
    def build(token: str):
        return Client("http://127.0.0.1:8081", sdkgen.HttpBearer(token))
    pass
