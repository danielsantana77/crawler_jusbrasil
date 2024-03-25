from courts.abstract_court import AbstractCourt


class FirstDegreeCeara(AbstractCourt):
    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
        self.state = "Ceará"
        self.degree = "1 grau"
        self.url_search_process = "https://esaj.tjce.jus.br/cpopg/search.do?"
        self.url_show_process = "https://esaj.tjce.jus.br/cpopg/sshow.do?"

    def get_url_show_process(self, process_code):
        return self.url_show_process + f'processo.codigo={process_code}'

    def get_url_search_process(self):
        return self.url_search_process + f'cbPesquisa=NUMPROC&dePesquisa={self.cnj}'
