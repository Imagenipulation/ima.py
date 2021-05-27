import asyncio
import aiohttp

import sys
from typing import Optional

from . import __version__


class HTTPClient:
    def __init__(self, token: str, loop = None) -> None:

        self.token = token
        self.loop = loop or asyncio.get_event_loop()

        self.__session = None

    def _headers(self) -> dict:
        return {"Authorization": self.token}

    def request(self):
        pass
