class Dog(object):
    def __init__(self, name): #init método construtor
        self.name = name #colocar o atributo
        print(f'Parabéns, sou {self.name} seu novo  cachorro')
    
    def sound(self, sound): #método sound
        print(f'{self.name} sou um cachorro, faço esse {sound} barulho')

#instância a classe caramelo
german_shepherd = Dog('Maira') #classe instanciada
german_shepherd_sound = german_shepherd.sound('auau') #classe instanciada

class Cat(object):
    def __init__(self, name): #init método construtor
        self.name = name #atributo
        print(f'Parabéns sou {self.name} seu novo gato.')
    
    def sound(self, sound):
        print(f'{self.name} {sound}')

white_cat = Cat('Branco')
white_cat_sound = white_cat.sound('miau')