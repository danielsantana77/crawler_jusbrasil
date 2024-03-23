from session.session import Session


class Controller:
    def __init__(self, cnj):
        self.cnj = str(cnj).replace('-', '').replace('.', '')
        self.session = Session().session
        self.courts_collect = None
        self.collections_result = {}

    def validate_cnj_process(self):
        if self.cnj != 20:
            return False
        return True

    def consult_process(self):
        if self.validate_cnj_process():
            return self.collect_data_in_courts()
        return {'Message': 'Invalid CNJ'}

    def define_courts_to_search(self):
        court = self.cnj[14:16]

    def collect_data_in_courts(self):
        courts = self.define_courts_to_search()
