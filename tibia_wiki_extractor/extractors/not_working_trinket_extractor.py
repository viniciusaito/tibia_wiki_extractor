from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.quiver import Quiver
from sqlalchemy import delete

session = generate_database_session()
session.query(Quiver).delete()

http_selector = generate_page_selector(url = 'https://www.tibiawiki.com.br/wiki/Extra_Slot')
table = apply_css_filters_on_selector(http_selector, ['table#tabelaDPL'])
table = table[0]
table = apply_css_filters_on_selector(http_selector, ['tr'])
column_list = {0:"name", 
               2:"attributes", 
               3:"weight"}
itens = extract_columns_from_table(column_list,table)

for item in itens:
    for n, text in enumerate(item):
        if item[n] == '':
            item[n] = '0'
    data_to_be_inserted = Quiver(name = item[0],
                                attributes = item[1],
                                weight = float(item[2]))
    session.add(data_to_be_inserted)

session.commit()
