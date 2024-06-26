from courts.abstract_court import AbstractCourt


class FirstDegreeAlagoas(AbstractCourt):
    def __init__(self, cnj):
        super().__init__()
        self.cnj = cnj
        self.state = "Alagoas"
        self.degree = "Primeiro grau"
        self.url_search_process = "https://www2.tjal.jus.br/cpopg/search.do?"
        self.url_show_process = "https://www2.tjal.jus.br/cpopg/show.do?"

    def get_url_show_process(self, process_code):
        pass

    def get_url_search_process(self):
        return self.url_search_process + f'cbPesquisa=NUMPROC&dePesquisa={self.cnj}'
