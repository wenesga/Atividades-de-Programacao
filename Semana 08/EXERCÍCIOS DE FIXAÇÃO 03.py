import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
3. Faça um programa que leia um vetor de 8 posições e, em seguida, leia dois 
   valores X e Y correspondentes a duas posições no vetor. Ao ﬁnal, o programa 
   deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.'''


vetor = np.random.randint(1, 20, 8)
print("Vetor = ", vetor)

x = vetor[2]
y = vetor[0]

soma = x + y

print(f'{x} + {y} = {soma}')
