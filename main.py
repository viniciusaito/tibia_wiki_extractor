from parsel import Selector
from httpx import get

response = get('https://www.tibiawiki.com.br/wiki/Armaduras').content
sel = Selector(text=response.decode())
filtro_1_pegar_a_tabela = 'table#tabelaDPL'
filtro_2_pegar_a_linha = 'tr'
numero_de_linhas_na_tabela = len(sel.css(filtro_1_pegar_a_tabela).css(filtro_2_pegar_a_linha))

def coletar_dado_da_linha(linha_da_tabela, tag_do_dado, numero_da_coluna=0, get_all=False):
    if get_all:
        dado = (linha_da_tabela
                    .css('td')[numero_da_coluna]
                    .css(f'{tag_do_dado}::text')
                    .getall())
    else:
        dado = (linha_da_tabela
                    .css('td')[numero_da_coluna]
                    .css(f'{tag_do_dado}::text')
                    .get())
    return dado 

for linha in range(1,numero_de_linhas_na_tabela):
    linha_da_tabela = sel.css(filtro_1_pegar_a_tabela).css(filtro_2_pegar_a_linha)[linha]
    
    nome_do_item = coletar_dado_da_linha(linha_da_tabela, 'a', 0)
    lvl_do_item = coletar_dado_da_linha(linha_da_tabela, 'small', 2)
    
    print(f'{linha}: "{nome_do_item}" "{lvl_do_item}"')
