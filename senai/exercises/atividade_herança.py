"""
Henrique Torres Campos
"""

#Classe Pai
class Pet(object):
    def __init__(self, nome): #método construtor
        self.nome = nome #atributo nome
    
class Cachorro(Pet):
    def __init__(self, nome):
        super().__init__(nome)

    def som_cachorro(self): 
        return (f'Sou {self.nome} e faço esse som AU AU.')

#Classe filho
class Gato(Pet):
    def __init__(self, nome):
        super().__init__(nome)

    def som_gato(self):
        return (f'Sou {self.nome} e faço esse som MIAU MIAU.')

#Classe filho
class Peixe(Pet):
    def __init__(self, nome):
        super().__init__(nome)

    def som_peixe(self):
        return (f'Sou o {self.nome} e faço esse som GLUB GLUB.')

#instânciando cachorro
cachorro = Cachorro('Hana')
print(cachorro.som_cachorro())

#instânciando gato
gato = Gato('Fred')
print(gato.som_gato())

#instânciando peixe
peixe = Peixe('Nemu')
print(peixe.som_peixe())        