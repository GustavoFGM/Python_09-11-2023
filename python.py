# ----------------------------------------------------------------------------#
# conjuntos(set)
# ex63
a = {'banana', 'abacate', 'ramen'}
b = {'ramen', 'abobora', 'abacaxi'}
uniao = a.union(b)
print(uniao)
# ----------------------------------------------------------------------------#

# ex64
a = {'banana', 'abacate', 'ramen'}
b = {'ramen', 'abobora', 'abacaxi'}
interseccao = a.intersection(b)
print(interseccao)
# ----------------------------------------------------------------------------#

# ex65
a = {'abobora', 'abacaxi', 'ramen'}
b = {'ramen', 'abobora', 'abacaxi', 1}
subconjunto = a.issubset(b)
# subconjunto = a <= b
print(subconjunto)
# ----------------------------------------------------------------------------#

# ex66
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
set1.discard(2)
print(set1)
# ----------------------------------------------------------------------------#

# ex67
a = {'abobora', 'abacaxi', 'ramen'}
b = {'ramen', 'abobora', 'abacaxi', 1}
c = a|b
# c = a.union(b)
print(c)
# ----------------------------------------------------------------------------#

# ex68
lista_duplicados = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
conjunto = set()
for x in lista_duplicados:
    conjunto.add(x)
print(conjunto)
# ou
lista_duplicados = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
conjunto = set(lista_duplicados)
print(conjunto)
# ----------------------------------------------------------------------------#

# ex69
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 5}
conjunto3 = conjunto1.difference(conjunto2)
if len(conjunto3) == 0:
    print('sao iguais')
else:
    print('sao diferentes')
# ou
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 5}
iguais = a == b
print(iguais)
# ----------------------------------------------------------------------------#

# ex70
def potencia(n):
    numeros = {2, 3, 4}
    for x in numeros:
        a = x**n
        print(a)
potencia(2)
# ----------------------------------------------------------------------------#

# ex71
conjunto = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6}
conjunto_sem_duplicada = set()
for elemento in conjunto:
    conjunto_sem_duplicada.add(elemento)
print(conjunto_sem_duplicada)
# ----------------------------------------------------------------------------#

# ex72-Desafio
def total_gasto_cliente(dados):
        
    

dados = [
    ('Gustavo', {'frango', 'arroz', 'feijão'}),
    ('Rodrigo', {'whey', 'cartas'}),
    ('Diego', {'monster', 'coca', 'pringles'})
]























