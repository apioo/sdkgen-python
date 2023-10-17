import requests
from requests import Session
from sdkgen.client_abstract import ClientAbstract
from sdkgen.authenticator import AuthenticatorInterface


class HttpClientFactory:
    def __init__(self, authenticator: AuthenticatorInterface):
        self.authenticator = authenticator

    def factory(self) -> Session:
        session = requests.Session()
        session.auth = self.authenticator
        session.headers['User-Agent'] = ClientAbstract.USER_AGENT
        session.headers['Accept'] = 'application/json'
        return session
