from courts.tjal import first_degree_al,second_degree_al
from courts.tjce import first_degree_ce,second_degree_ce

dict_courts = {
    '02' : [first_degree_al.FirstDegreeAlagoas, second_degree_al.SecondDegreeAlagoas],
    '06' : [first_degree_ce.FirstDegreeCeara, second_degree_ce.SecondDegreeCeara]
}
