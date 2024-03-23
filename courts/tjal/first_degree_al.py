class FirstDegreeAlagoas:
    def __init__(self, cnj):
        self.cnj = cnj
        self.state = "AL"
        self.degree = "1 grau"
        self.url_search_process = "https://www2.tjal.jus.br/cpopg/search.do?"
        self.url_show_process = "https://www2.tjal.jus.br/cpopg/show.do?"

    def get_url_show_process(self):
        return self.url_show_process + f'processo.numero={self.cnj}'

