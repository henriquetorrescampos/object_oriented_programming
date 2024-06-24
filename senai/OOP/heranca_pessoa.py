class Pessoa(object):
    def __init__(self, nome): #construtor
        self.nome = nome

    def get_nome(self): #self se refere a classe Pessoa
        return self.nome

class Pessoa_fisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf =  cpf
    
    def get_cpf(self):
        return self.cpf

class Pessoa_juridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj

andre = Pessoa_fisica('Andre', '700.000.000-00')
print(andre.get_nome())
print(andre.get_cpf())

google = Pessoa_juridica('Google', '0001/000.000.000')
print(google.get_nome())
print(google.get_cnpj())