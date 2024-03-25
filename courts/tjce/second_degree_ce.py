from courts.abstract_court import AbstractCourt


class SecondDegreeCeara(AbstractCourt):
    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
        self.state = "CE"
        self.degree = "2 grau"
        self.url_search_process = "https://esaj.tjce.jus.br/cposg5/search.do?"
        self.url_show_process = "https://esaj.tjce.jus.br/cposg5/show.do?"

    def get_url_show_process(self, process_code):
        return self.url_show_process + f'processo.codigo={process_code}'

    def get_url_search_process(self):
        return self.url_search_process + f'cbPesquisa=NUMPROC&dePesquisa={self.cnj}'
