class Movement:
    def __init__(self,date,movement,description):
        self.date = date
        self.movement = movement
        self.description = description


    def to_json(self):
        return {
            'Data': self.date,
            'Movimentação': self.movement,
            'Descrição': self.description
        }