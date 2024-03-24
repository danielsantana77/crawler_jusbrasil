from session.session import Session
from courts.available_courts import dict_courts
from bs4 import BeautifulSoup

class Controller:
    def __init__(self, cnj):
        self.cnj = str(cnj).replace('-', '').replace('.', '')
        self.court_code = self.cnj[14:16]
        self.session = Session()
        self.courts_collect = None
        self.collections_result = {}

    def validate_cnj_process(self):
        if len(self.cnj) != 20 or self.court_code in dict_courts is False:
            return False
        return True

    def consult_process(self):
        if self.validate_cnj_process():
            return self.collect_data_in_courts()
        return {'Message': 'Invalid CNJ'}

    def collect_code_process_in_page(self, html, court):
        soap = BeautifulSoup(html, 'html.parser')
        if "processoSelecionado" in html:
            process_code = soap.find('input', {'id' :'processoSelecionado'})['value']
            html = self.session.get_html_in_site(court.get_url_show_process(process_code))
        return html


    def collect_data_in_courts(self):
        list_courts = dict_courts[self.court_code]
        for court in list_courts:
            court_obj = court(self.cnj)
            html = self.session.get_html_in_site(court_obj.get_url_search_process())
            html = self.collect_code_process_in_page(html, court_obj)

        return {'Message': 'Em construção'}