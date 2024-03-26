from controller.controller import Controller

cnj = '0070337-91.2008.8.06.0001'
controller = Controller(cnj)
controller.consult_process()
process_data = controller.collections_result['Ceará Segundo grau']


def test_quantity_of_parts():
    assert len(process_data['Partes Envolvidas'][0]) > 0


def test_quantity_of_movements():
    assert len(process_data['Movimentações']) > 0


def test_claim_value():
    assert process_data["Valor da Ação"] == "Indisponivel"


def test_judge_result():
    assert process_data['Juiz'] == 'Indisponivel'


def test_distribution_date_result():
    assert process_data['Data de Distribuição'] == 'Indisponivel'


def test_subject_result():
    assert process_data['Assunto'] == 'Crimes de Trânsito'


def test_area_result():
    assert process_data['Área'] == 'Criminal'


def test_class_result():
    assert process_data['Classe'] == 'Apelação Criminal'


def test_quantity_of_results():
    assert len(controller.collections_result) == 2
