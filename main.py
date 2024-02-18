from tibia_wiki_extractor.extraction import *
from tibia_wiki_extractor.database.connector import *
from tibia_wiki_extractor.database.tables.armor import Armor
from sqlalchemy import delete

engine = generate_database_engine()
session = generate_database_session(engine)
session.query(Armor).delete()

http_selector = generate_page_selector(url = 'https://www.tibiawiki.com.br/wiki/Armaduras')
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
armors = extract_columns_from_table(column_list,table)

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
