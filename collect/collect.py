from bs4 import BeautifulSoup

from model.process import Process


class Collect:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.process = Process()

    def collect_data(self):
        self.process.set_area(self.collect_area())
        self.process.set_subject(self.collect_subject())
        self.process.set_distribution_date(self.collect_distribution_date())
        self.process.set_juridic_class(self.collect_juridic_class())
        self.process.set_claim_value(self.collect_claim_value())
        self.process.set_parts_involved(self.collect_parts_involved())
        self.process.set_list_of_movements(self.collect_movements_of_process())
        self.process.set_judge(self.collect_judge())

    def collect_juridic_class(self):
        juridic_class = self.soup.find(id='classeProcesso')
        if not juridic_class:
            return "Indisponivel"
        return self.__format_text(juridic_class.text)

    def collect_area(self):
        area = self.soup.find('div', {'id': 'areaProcesso'})
        if not area:
            return "Indisponivel"
        return self.__format_text(area.text)

    def collect_subject(self):
        subject = self.soup.find(id='assuntoProcesso')
        if not subject:
            return "Indisponivel"
        return self.__format_text(subject.text)

    def collect_distribution_date(self):
        distribution_date = self.soup.find(id='dataHoraDistribuicaoProcesso')
        if not distribution_date:
            return "Indisponivel"
        return self.__format_text(distribution_date.text)

    def collect_judge(self):
        judge = self.soup.find(id='juizProcesso')
        if not judge:
            return "Indisponivel"
        return self.__format_text(judge.text)

    def collect_claim_value(self):
        claim_value = self.soup.find(id='valorAcaoProcesso')
        if not claim_value:
            return "Indisponivel"
        return self.__format_text(claim_value.text)

    @staticmethod
    def __format_text(text):
        text = text.replace('\t', '').strip().split('\n')[0]
        return text

    def __get_parts_in_element(self, parts):
        involved_list = []
        for elem in iter(parts):
            if not 'span' in str(elem):
                part_name = self.__format_text(elem.text)
                if part_name: involved_list.append(self.__format_text(elem.text))

        return involved_list

    def collect_parts_involved(self):
        list_of_parts = []
        dict_of_parts = {}
        parts_involved = self.soup.find('table', {'id': 'tablePartesPrincipais'})
        trs = parts_involved.findAll('tr')
        for tr in trs:
            part_type = tr.find('span', {'class': 'mensagemExibindo tipoDeParticipacao'}).text
            part = tr.find('td', {'class': 'nomeParteEAdvogado'})
            parts = self.__get_parts_in_element(part)
            part_type = self.__format_text(part_type)
            dict_of_parts[part_type] = parts
        list_of_parts.append(dict_of_parts)

        return list_of_parts

    def __collect_date(self, element):
        date = element.find('td', {'class': 'dataMovimentacao'})
        if not date:
            date = element.find('td', {'class': 'dataMovimentacaoProcesso'})
        return self.__format_text(date.text)

    @staticmethod
    def __collect_description_element(element):
        td_moviment = element.find('td', {'class': 'descricaoMovimentacao'})
        if not td_moviment:
            td_moviment = element.find('td', {'class': 'descricaoMovimentacaoProcesso'})
        return td_moviment

    def collect_movements_of_process(self):
        list_of_movements = []
        table = self.soup.find('tbody', {'id': 'tabelaUltimasMovimentacoes'})
        trs = table.findAll('tr')
        for tr in trs:
            date = self.__collect_date(tr)
            td_movement = self.__collect_description_element(tr)
            link = td_movement.find('a')
            movement = link.text if link else td_movement.text
            movement = self.__format_text(movement)
            description = self.__format_text(tr.find('span').text)
            list_of_movements.append((date, movement, description))

        return list_of_movements
