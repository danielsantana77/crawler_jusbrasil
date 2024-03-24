from bs4 import BeautifulSoup

from process.process import Process


class Collect:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.process = Process()
        self.collect_data()

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
        juridic_class = self.soup.find('span', {'id': 'classeProcesso'})
        if juridic_class:
            return juridic_class.text
        juridic_class = self.soup.find('div', {'id': 'classeProcesso'}).findChild('span')
        return juridic_class.text

    def collect_area(self):
        div = self.soup.find('div', {'id': 'areaProcesso'})
        area = div.find('span').text
        return area

    def collect_subject(self):
        subject = self.soup.find('span', {'id': 'assuntoProcesso'})
        if not subject:
            div = self.soup.find('div', {'id': 'assuntoProcesso'})
            subject = div.find('span')
        return subject.text

    def collect_distribution_date(self):
        distribution_date = self.soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
        if not distribution_date:
            return "Indisponivel"
        return distribution_date.text

    def collect_judge(self):
        judge = self.soup.find('span', {'id': 'juizProcesso'})
        if not judge:
            return "Indisponivel"
        return judge.text

    def collect_claim_value(self):
        claim_value = self.soup.find('div', {'id': 'valorAcaoProcesso'})
        if not claim_value:
            return "Indisponivel"
        return claim_value.text

    def __format_text(self, text):
        text = text.replace('\t', '').strip().split('\n')[0]
        return text

    def collect_parts_involved(self):
        list_of_parts = []
        dict_of_parts = {}
        parts_involved = self.soup.find('table', {'id': 'tablePartesPrincipais'})
        trs = parts_involved.findAll('tr')
        for tr in trs:
            part_type = tr.find('span', {'class': 'mensagemExibindo tipoDeParticipacao'}).text
            part = tr.find('td', {'class': 'nomeParteEAdvogado'}).text
            part = self.__format_text(part)
            part_type = self.__format_text(part_type)
            dict_of_parts[part_type] = part
        list_of_parts.append(dict_of_parts)

        return list_of_parts

    def collect_movements_of_process(self):
        list_of_movements = []
        table = self.soup.find('tbody', {'id': 'tabelaUltimasMovimentacoes'})
        trs = table.findAll('tr')
        for tr in trs:
            date = tr.find('td', {'class': 'dataMovimentacao'})
            if not date:
                date = tr.find('td', {'class': 'dataMovimentacaoProcesso'})
            date = self.__format_text(date.text)
            td_moviment = tr.find('td', {'class': 'descricaoMovimentacao'})
            if not td_moviment:
                td_moviment = tr.find('td', {'class': 'descricaoMovimentacaoProcesso'})
            link = td_moviment.find('a')
            movement = link.text if link else td_moviment.text
            movement = self.__format_text(movement)
            description = self.__format_text(tr.find('span').text)
            list_of_movements.append(
                {'Data': date,
                 'Movimento': movement,
                 'Descrição': description}
            )
        return list_of_movements
