from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.armor import Armor

url= 'https://www.tibiawiki.com.br/wiki/Armaduras'
filters = ['table#tabelaDPL','tr']
http_selector = generate_page_selector(url)
table = apply_css_filters_on_selector(http_selector, filters)

num_of_rows_in_table = len(table)

armors = []
column_list = {0:"name", 
               2:"level", 
               3:"vocation", 
               4:"slots", 
               5:"tier_class", 
               6:"defense", 
               7:"bonus", 
               8:"protection", 
               9:"weight"}
for row in range(1,num_of_rows_in_table):
    string_list = []
    table_row = table[row]
    for column in column_list:
        data = getall_text_from_table_row(table_row, column)
        string_list.append(data)
    armors.append(string_list)

engine = generate_database_engine()
session = generate_database_session(engine)

for armor in armors:
    if armor[5] == '':
        armor[5] = '0'
    data_to_be_inserted = Armor(name = armor[0],
                                level = int(armor[1]),
                                vocation = armor[2],
                                slots = int(armor[3]),
                                tier_class = int(armor[4]),
                                defense = int(armor[5]),
                                bonus = armor[6],
                                protection = armor[7],
                                weight = float(armor[8]))
    session.add(data_to_be_inserted)

session.commit()
