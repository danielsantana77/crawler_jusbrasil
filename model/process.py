from model.movement import Movement


class Process:
    def __init__(self):
        self.juridic_class = ''
        self.area = ''
        self.subject = ''
        self.distribution_date = ''
        self.judge = ''
        self.claim_value = ''
        self.parts_involved = []
        self.list_of_movements = []

    def to_json(self):
        return {
            'Classe': self.juridic_class,
            'Área': self.area,
            'Assunto': self.subject,
            'Data de distribuicao': self.distribution_date,
            'Juiz': self.judge,
            'Valor da Ação': self.claim_value,
            'Partes Envolvidas': self.parts_involved,
            'Movimentações': [movements.to_json() for movements in self.list_of_movements]
        }

    def set_juridic_class(self, juridic_class):
        self.juridic_class = juridic_class

    def set_area(self, area):
        self.area = area

    def set_subject(self, subject):
        self.subject = subject

    def set_distribution_date(self, distribution_date):
        self.distribution_date = distribution_date

    def set_judge(self, judge):
        self.judge = judge

    def set_claim_value(self, claim_value):
        self.claim_value = claim_value

    def set_parts_involved(self, parts_involved):
        self.parts_involved = parts_involved

    def set_list_of_movements(self, list_of_movements):
        for movement in list_of_movements:
            date, movement,description = movement
            self.list_of_movements.append(Movement(date, movement,description))
