import base64
from requests.auth import AuthBase
from sdkgen.credentials import CredentialsInterface, HttpBasic, HttpBearer, ApiKey, OAuth2, Anonymous
from sdkgen.exceptions import InvalidCredentialsException


class AuthenticatorInterface(AuthBase):
    pass


class AuthenticatorFactory:
    @staticmethod
    def factory(credentials: CredentialsInterface):
        if isinstance(credentials, HttpBasic):
            return HttpBasicAuthenticator(credentials)
        elif isinstance(credentials, HttpBearer):
            return HttpBearerAuthenticator(credentials)
        elif isinstance(credentials, ApiKey):
            return ApiKeyAuthenticator(credentials)
        elif isinstance(credentials, OAuth2):
            return OAuth2Authenticator(credentials)
        elif isinstance(credentials, Anonymous):
            return AnonymousAuthenticator(credentials)
        else:
            raise InvalidCredentialsException("Could not find authenticator for credentials")
        pass


class AnonymousAuthenticator(AuthenticatorInterface):
    def __init__(self, credentials: Anonymous):
        self.credentials = credentials

    def __call__(self, request):
        pass


class ApiKeyAuthenticator(AuthenticatorInterface):
    def __init__(self, credentials: ApiKey):
        self.credentials = credentials

    def __call__(self, request):
        request.headers[self.credentials.name] = self.credentials.token
        pass


class HttpBasicAuthenticator(AuthenticatorInterface):
    def __init__(self, credentials: HttpBasic):
        self.credentials = credentials

    def __call__(self, request):
        request.headers["Authorization"] = "Basic " + str(base64.b64encode(self.credentials.username + ":" + self.credentials.password))
        pass


class HttpBearerAuthenticator(AuthenticatorInterface):
    def __init__(self, credentials: HttpBearer):
        self.credentials = credentials

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.credentials.token
        pass


class OAuth2Authenticator(AuthenticatorInterface):
    def __init__(self, credentials: OAuth2):
        self.credentials = credentials

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.get_access_token()
        pass

    def get_access_token(self) -> str:
        return ""
