from controller.controller import Controller

cnj = '0710802-55.2018.8.02.0001'
controller = Controller(cnj)
controller.consult_process()
process_data = controller.collections_result['Alagoas Segundo grau']


def test_quantity_of_parts():
    assert len(process_data['Partes Envolvidas'][0]) > 0


def test_quantity_of_movements():
    assert len(process_data['Movimentações']) > 0


def test_claim_value():
    assert process_data["Valor da Ação"] == "281.178,42"


def test_judge_result():
    assert process_data['Juiz'] == 'Indisponivel'


def test_distribution_date_result():
    assert process_data['Data de Distribuição'] == 'Indisponivel'


def test_subject_result():
    assert process_data['Assunto'] == 'Obrigações'


def test_area_result():
    assert process_data['Área'] == 'Cível'


def test_class_result():
    assert process_data['Classe'] == 'Apelação Cível'


def test_quantity_of_results():
    assert len(controller.collections_result) == 2
