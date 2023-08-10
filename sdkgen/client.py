from sdkgen.authenticator import AuthenticatorFactory
from sdkgen.credentials import CredentialsInterface
from sdkgen.http_client_factory import HttpClientFactory
from sdkgen.parser import Parser
from requests import Session


class ClientAbstract:
    USER_AGENT = "SDKgen Client v1.0"

    def __init__(self, base_url: str, credentials: CredentialsInterface):
        self.authenticator = AuthenticatorFactory.factory(credentials)
        self.http_client = HttpClientFactory(self.authenticator).factory()
        self.parser = Parser(base_url)

    pass


class TagAbstract:
    def __init__(self, http_client: Session, parser: Parser):
        self.http_client = http_client
        self.parser = parser
