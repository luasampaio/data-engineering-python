# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


#Argumento 

leao = Animal(nome='Leão')  #instancia da classe  # classe também pode ter um namespace 
print(leao.nome)
print(leao.executar('maçã'))

