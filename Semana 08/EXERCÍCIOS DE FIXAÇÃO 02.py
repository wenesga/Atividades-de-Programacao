def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
2. Leia um conjunto de números reais, armazenando-os em um vetor, e calcule o 
   quadrado de cada componente desse vetor, armazenando o resultado em outro 
   vetor. Ambos os conjuntos possuem 10 elementos. Imprima os conjuntos.    '''

conjunto = set()
sqrt_conjunto = set()

for i in range(5):
    num_real = float(input(f"{i+1} numero real: "))
    conjunto.add(num_real)

for num_real in conjunto:
    sqrt_conjunto.add(num_real ** 2)

print(f'Conjunto: {conjunto}')
print(f'Quadrado de Conjunto: {sqrt_conjunto}')
