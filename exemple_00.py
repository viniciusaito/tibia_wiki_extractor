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

def coletar_dado_com_multiplas_tags_da_linha(linha_da_tabela, lista_de_tags_do_dado, numero_da_coluna=0):
    dado = ''
    for tag_do_dado in lista_de_tags_do_dado:
        dado_placeholder = coletar_dado_da_linha(linha_da_tabela, tag_do_dado, numero_da_coluna)
        if dado_placeholder != None:
            dado = f'{dado}{dado_placeholder}'
    return dado

def coletar_dado_com_multiplas_tags(linha_da_tabela, 
                                    lista_de_tags_do_dado, 
                                    numero_da_coluna=0):
    dado = ''
    for tag in lista_de_tags_do_dado:
        dado_placeholder = coletar_dado_da_linha(linha_da_tabela, 
                                                 tag, 
                                                 numero_da_coluna, 
                                                 get_all=True)
    return dado
        

for linha in range(1,numero_de_linhas_na_tabela):
    linha_da_tabela = sel.css(filtro_1_pegar_a_tabela).css(filtro_2_pegar_a_linha)[linha]
    
    nome_do_item = coletar_dado_da_linha(linha_da_tabela, 'a', 0)
    lvl_do_item = coletar_dado_da_linha(linha_da_tabela, 'small', 2)
    voc_do_item = coletar_dado_com_multiplas_tags_da_linha(
        linha_da_tabela, 
        ['a[title="Sorcerer"]','a[title="Knight"]','small','a[title="Druid"]','a[title="Paladin"]'], 
        3)
    slots_do_item = coletar_dado_da_linha(linha_da_tabela, '*', 4)
    tier_do_item = coletar_dado_da_linha(linha_da_tabela, '*', 5)
    armor_do_item = coletar_dado_da_linha(linha_da_tabela, '*', 6)
    
    print(f'{linha}: "{nome_do_item}" "{lvl_do_item}" "{voc_do_item}" "{slots_do_item}" "{tier_do_item}" "{armor_do_item}"')
