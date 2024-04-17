
cardapio ={
    100:{'produto': 'canhorro quente', 'preço':1.20},
    101:{'produto': 'bauru simples', 'preço':1.30},
    102:{'produto': 'bauru com ovo', 'preço':1.50},
    103:{'produto': 'hamburguer', 'preço':1.20},
    104:{'produto': 'cheeseburguer', 'preço':1.70},
    105:{'produto': 'suco', 'preço':2.20},
    106:{'produto': 'refrigerante', 'preço':1.00},
}

codigo_produto = int(input('digite o codigo do produto: '))
quantidade = int(input('digite a quantidade: '))

if codigo_produto in cardapio:
    produto = cardapio[codigo_produto]['produto']
    preco_unitario = cardapio[codigo_produto]['preço']
    
    valor_total = quantidade * preco_unitario
    
    print(f'o total a ser pago pelo {quantidade} {produto}(s) é R${valor_total:.2f}.' )
else:
    print('código do produto inválido.')
