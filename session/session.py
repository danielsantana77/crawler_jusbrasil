import requests

from session.tls_adapter import TLSAdapter


class Session:
    def __init__(self):
        self.session = self.define_session()

    def define_session(self):
        session = requests.Session()
        session.mount("https://", TLSAdapter())
        return session

    def get_html_in_site(self, link):
        response = self.session.get(link)
        return response.text
