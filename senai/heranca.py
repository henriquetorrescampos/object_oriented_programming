import datetime

#Classe pai
class Pet(object):
    def __init__(self, nome, idade):
        self.nome = nome #método nome
        self.idade = idade #método idade
    
    def set_idade(self, idade):
        self.idade = idade
    
    def get_idade(self):
        return datetime.date.today().year - self.idade
    
#Classe filho
class Dog(Pet):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def som(self):
        return f'A {self.nome} faz AU-AU '

labrador = Dog('Stela', 13) #criação da instância
print(labrador.nome) #retorna o nome Stela
print(labrador.idade) #retorna a idade Stela
print(labrador.som())


#Classe filho
class Cat(Pet):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def som(self):
        return f'O {self.nome} faz MIAU-MIAU'