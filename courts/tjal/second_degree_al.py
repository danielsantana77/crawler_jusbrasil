class SecondDegreeAlagoas:
    def __init__(self, cnj):
        self.cnj = cnj
        self.state = "AL"
        self.degree = "2 grau"
        self.url_search_process = "https://www2.tjal.jus.br/cpopg5/search.do?"
        self.url_show_process = "https://www2.tjal.jus.br/cpopg5/show.do?"

    def get_url_show_process(self,process_code):
        return self.url_show_process + f'processo.codigo={process_code}'

    def get_url_search_process(self):
        return self.url_search_process + f'cbPesquisa=NUMPROC&dePesquisa={self.cnj}'
