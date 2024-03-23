import requests
from requests.adapters import HTTPAdapter
from session.tls_adapter import TLSAdapter

class Session:
    def __init__(self):
        self.session = self.define_session()

    def define_session(self):
        session = requests.Session()
        session.mount("https://", TLSAdapter())
        return session