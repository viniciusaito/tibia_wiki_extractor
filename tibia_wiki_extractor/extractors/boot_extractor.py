from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.boot import Boots
from sqlalchemy import delete

session = generate_database_session()
session.query(Boots).delete()

http_selector = generate_page_selector(url = 'https://www.tibiawiki.com.br/wiki/Botas')
table = apply_css_filters_on_selector(http_selector, ['table#tabelaDPL','tr'])
column_list = {0:"name", 
               2:"level", 
               3:"vocation", 
               4:"slots", 
               5:"tier_class", 
               6:"defense", 
               7:"bonus", 
               8:"protection", 
               9:"weight"}
itens = extract_columns_from_table(column_list,table)

for item in itens:
    for n, text in enumerate(item):
        if item[n] == '':
            item[n] = '0'
    data_to_be_inserted = Boots(name = item[0],
                                level = int(item[1]),
                                vocation = item[2],
                                slots = int(item[3]),
                                tier_class = int(item[4]),
                                defense = int(item[5]),
                                bonus = item[6],
                                protection = item[7],
                                weight = float(item[8]))
    session.add(data_to_be_inserted)

session.commit()
