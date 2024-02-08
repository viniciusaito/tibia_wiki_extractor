from parsel import Selector
from httpx import get

def generate_page_selector(url):
    """Returns a selector of the url
    Parameters
    ----------
    url : str
        URL that will be turned into a selector
    """
    response = get('https://www.tibiawiki.com.br/wiki/Armaduras').content
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

def collect_text_from_selector_row(table_row_selector, filters, row_number=0, get_all=False):
    """ Collect data from a selectors row, it can collect one or all elements inside that row.
    Parameters
    ----------
    sel : sel
        A parsel selector
    sel : sel
        A parsel selector
    filters : list
        List of filters that will be applied to the selector
    """
    if get_all:
        text = (table_row_selector
                    .css('td')[row_number]
                    .css(f'{filters}::text')
                    .getall())
    else:
        text = (table_row_selector
                    .css('td')[row_number]
                    .css(f'{filters}::text')
                    .get())
    return text

def getall_text_from_table_row(table_row, row_number):
    text_data = apply_css_filters_on_selector(table_row, ['td'])
    table_data = text_data[row_number]
    list_of_text_data = table_data.css('::text').getall()
    list_of_text_data = [string for string in list_of_text_data if string != '\n']
    final_string = ''.join(list_of_text_data)
    
    return final_string
