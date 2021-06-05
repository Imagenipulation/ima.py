from .core.http import HTTPClient


class Client:
    def __init__(self, token: str, loop = None) -> None:
        self.http = HTTPClient(token, loop)
