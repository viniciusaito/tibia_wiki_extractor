from parsel import Selector
from httpx import get

def generate_page_selector(url):
    """Returns a selector of the url
    Parameters
    ----------
    url : str
        URL that will be turned into a selector
    """
    response = get(url).content
    sel = Selector(text=response.decode())
    return sel

def apply_css_filters_on_selector(sel, filters):
    """Returns a selector but with all css filters applied on it
    Parameters
    ----------
    sel : selector
        A parsel selector
    filters : list
        List of filters that will be applied to the selector
    """
    for filter in filters:
        sel = sel.css(filter)

    return sel

def getall_text_from_table_row(table_row, row_number):
    """ Get all text from a TD element and remove line breaks from it
    Parameters
    ----------
    table_row : selector
        A parsel selector
    row_number : int
        The number of the row that the text will be extracted
    """
    text_data = apply_css_filters_on_selector(table_row, ['td'])
    table_data = text_data[row_number]
    list_of_text_data = table_data.css('::text').getall()
    list_of_text_data = [string for string in list_of_text_data if string != '\n']
    joined_string = ''.join(list_of_text_data)
    final_string = joined_string.replace('\n','')
    
    return final_string

def extract_columns_from_table(column_list, table):
    """ Extract specific columns from a table, can use either list of columns or dict
    Parameters
    ----------
    column_list : list, dict
        List of columns that will be extracted from the table
    table : selector
        Selector in a table, can be created by using function apply_css_filters_on_selecter to filter a table.
    """
    num_of_rows_in_table = len(table)
    armors = []
    for row in range(1,num_of_rows_in_table):
        string_list = []
        table_row = table[row]
        for column in column_list:
            data = getall_text_from_table_row(table_row, column)
            string_list.append(data)
        armors.append(string_list)

    return armors
