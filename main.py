from parsel import Selector
from httpx import get
from tibia_wiki_extractor.extraction import generate_page_selector, apply_css_filters_on_selector, collect_text_from_selector_row

url= 'https://www.tibiawiki.com.br/wiki/Armaduras'
filters = ['table#tabelaDPL','tr']
sel = generate_page_selector(url)
table_row_selector = apply_css_filters_on_selector(sel, filters)

num_of_rows_in_table = len(table_row_selector)

for row in range(1,num_of_rows_in_table):
    table_row = table_row_selector[row]
    
    item_name = collect_text_from_selector_row(table_row, 'a', 0)
    item_level = collect_text_from_selector_row(table_row, 'small', 2)
    
    print(f'{row}: "{item_name}" "{item_level}"')
