limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''2. Crie uma lista de tuplas para armazenar informações de produtos em uma loja. 
Cada tupla deve conter o nome, preço e quantidade disponível de um produto.'''

produtos = [("Arroz", 40.0, 10), # lista de tuplas
            ("Feijão", 20, 5),
            ("Açucar", 15, 6)
]
print(produtos,'\n')

for produto in produtos: 
    print(produto[0], produto[1], produto[2]) # 1ª forma de imprimir
print()

# =============================================================================

for nome, preco, quantidade in produtos: 
    print(nome, preco, quantidade) # 1ª forma de imprimir
print()

# =============================================================================
    
produtos_dict = [] # lista de dicionário

for nome, preco, quantidade in produtos:
    produtos_dict.append({
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

print(produtos_dict)

