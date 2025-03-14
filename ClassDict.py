
#collection 
from collections import defaultdict

cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]

cores_favoritas = defaultdict(list)

for chave, valor in cores:
    cores_favoritas[chave].append(valor)

print(type(cores_favoritas))