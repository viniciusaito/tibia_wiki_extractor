from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.quiver import Quiver
from sqlalchemy import delete

session = generate_database_session()
session.query(Quiver).delete()

http_selector = generate_page_selector(url = 'https://www.tibiawiki.com.br/wiki/Aljavas')
table = apply_css_filters_on_selector(http_selector, ['table#tabelaDPL','tr'])
column_list = {0:"name", 
               2:"level", 
               3:"vocation", 
               4:"volume", 
               5:"bonus", 
               6:"protection", 
               7:"weight"}
itens = extract_columns_from_table(column_list,table)

for item in itens:
    for n, text in enumerate(item):
        if item[n] == '':
            item[n] = '0'
    data_to_be_inserted = Quiver(name = item[0],
                                level = int(item[1]),
                                vocation = item[2],
                                volume = int(item[3]),
                                bonus = item[4],
                                protection = item[5],
                                weight = float(item[6]))
    session.add(data_to_be_inserted)

session.commit()
