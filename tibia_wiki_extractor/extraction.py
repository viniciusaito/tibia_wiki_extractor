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
    """Returns a selector but with all css filters applyed on it
    Parameters
    ----------
    sel : sel
        A parsel selector
    filters : list
        List of filters that will be applied to the selector
    """
    for filter in filters:
        sel = sel.css(filter)

    return sel

def getall_text_from_table_row(table_row, row_number):
    text_data = apply_css_filters_on_selector(table_row, ['td'])
    table_data = text_data[row_number]
    list_of_text_data = table_data.css('::text').getall()
    list_of_text_data = [string for string in list_of_text_data if string != '\n']
    final_string = ''.join(list_of_text_data)
    
    return final_string
