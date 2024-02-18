from tibia_wiki_extractor.extraction import *

url= 'https://www.tibiawiki.com.br/wiki/Armaduras'
filters = ['table#tabelaDPL','tr']
http_selector = generate_page_selector(url)
table = apply_css_filters_on_selector(http_selector, filters)

num_of_rows_in_table = len(table)

# string_list = []
# for row in range(1,num_of_rows_in_table):
#     table_row = table[row]

#     item_name = getall_text_from_table_row(table_row, 0)
#     item_level = getall_text_from_table_row(table_row, 2)
#     item_vocation = getall_text_from_table_row(table_row, 3)
#     item_protection = getall_text_from_table_row(table_row, 7)
    
#     print(f'{row}: "{item_name}" "{item_level}" "{item_vocation}" "{item_protection}"')

string_list_2 = []
column_list = [0,2,3,4,5,6,7,8,9]
for row in range(1,num_of_rows_in_table):
    string_list = []
    table_row = table[row]
    for column in column_list:
        data = getall_text_from_table_row(table_row, column)
        string_list.append(data)
    string_list_2.append(string_list)

for armor in string_list_2:
    print(armor)
