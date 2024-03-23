class SecondDegreeCeara:
    def __init__(self):
        self.url_show = "https://esaj.tjce.jus.br/cposg5/show.do?"

    def get_data_link(self,process_code):
        return self.url + f'processo.codigo={process_code}'