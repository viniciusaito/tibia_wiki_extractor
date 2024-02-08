from parsel import Selector
from httpx import get
from tibia_wiki_extractor.extraction import *

url= 'https://www.tibiawiki.com.br/wiki/Armaduras'
filters = ['table#tabelaDPL','tr']
sel = generate_page_selector(url)
table = apply_css_filters_on_selector(sel, filters)

num_of_rows_in_table = len(table)

for row in range(1,num_of_rows_in_table):
    table_row = table[row]

    item_name = collect_text_from_selector_row(table_row, 'a', 0)
    item_level = collect_text_from_selector_row(table_row, 'small', 2)
    item_vocation = getall_text_from_table_row(table_row, 3)
    
    print(f'{row}: "{item_name}" "{item_level}" "{item_vocation}"')
