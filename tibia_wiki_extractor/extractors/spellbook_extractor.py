from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.spellbook import Spellbook
from sqlalchemy import delete

session = generate_database_session()
session.query(Spellbook).delete()

http_selector = generate_page_selector(url = 'https://www.tibiawiki.com.br/wiki/Spellbooks')
table = apply_css_filters_on_selector(http_selector, ['table#tabelaDPL','tr'])
column_list = {0:"name", 
               2:"level", 
               3:"vocation", 
               4:"slots", 
               5:"defense", 
               6:"bonus", 
               7:"protection", 
               8:"weight"}
itens = extract_columns_from_table(column_list,table)

for item in itens:
    for n, text in enumerate(item):
        if item[n] == '':
            item[n] = '0'
    data_to_be_inserted = Spellbook(name = item[0],
                                level = int(item[1]),
                                vocation = item[2],
                                slots = int(item[3]),
                                defense = int(item[4]),
                                bonus = item[5],
                                protection = item[6],
                                weight = float(item[7]))
    session.add(data_to_be_inserted)

session.commit()
