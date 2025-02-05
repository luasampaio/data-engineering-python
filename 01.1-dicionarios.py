# Description: Dicionários em Python
Paises = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' , 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' , 'brazil':'brasilia'}


# 1. Imprima

print(Paises.keys())
print(Paises['norway'])


# 2. Adicione um novo país
Paises['germany'] = 'berlin'

# 3. imprimindo o dicionário
print(Paises)

# 4. Remova um país
del(Paises['norway'])

# 5. imprimindo o dicionário
print(Paises)

# 6. Verifique se um país está no dicionário01-dicionarios.py
print('norway' in Paises)

# 7. Limpe o dicionário
#Paises.clear()

# 8. imprimindo o dicionário 
# print(Paises)


# 9. Deletando o dicionário
#del(Paises)

# 10. imprimindo o dicionário
Paises["Japan"] = 'tokyo'

print(Paises)