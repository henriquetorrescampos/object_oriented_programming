import datetime

class Dog(object):
    def __init__(self, name, hight, age): #init método construtor, #self representa objeto que cria
        self.name = name #colocar o atributo, os atributos aqui são globais dentro dos métodos
        self.hight = hight #atributo hight
        self.age = age
        print(f'Parabéns, sou {self.name} seu novo cachorro.')
    
    def sound(self, sound): #método sound, variável sound é local
        print(f'{self.name} sou um cachorro, faço esse {sound} barulho ')
    
    def hight_(self, sound): #sound é uma parametro local
        print(f'A altura da {self.name} é {self.hight} e o seu som é {sound}')

    def age_(self):
        return datetime.date.today().year - self.age
    
    def birthday_date(self, year_birth):
        self.birth_date = year_birth
        print(self.birth_date)
        
#instância a classe Dog
german_shepherd = Dog('Maira', 1.80, 2015) #classe Dog instanciada 
german_shepherd_sound = german_shepherd.sound('auau') #class Dog e o método sound estanciado
german_shepherd_hight = german_shepherd.hight_('AUAU') #class Dog e o método hight estanciado
print(german_shepherd.age_())
german_shepherd.birthday_date(2010)
print('idade:', german_shepherd.age_())


class Cat(object):
    def __init__(self, name, color): #init método construtor
        self.name = name #atributo name
        self.color = color #atributo color
        print(f'Parabéns sou {self.name} seu novo gato e a minha cor é {self.color}.')
    
    def sound(self, sound):
        print(f'{self.name} {sound}')

white_cat = Cat('Bob', 'Black')
white_cat_sound = white_cat.sound('miau')
