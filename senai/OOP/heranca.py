
class Animal(object):
    def __init__(self, color, name, sound, walk, run):
        self.color = color #atributos
        self.name = name #atributos
        self.sound = sound #atributos
        self.walk = walk #atributos
        self.run = run #atributos

    def Sound(self): #método
        return self.sound
    
    def Walk(self): #método
        return self.walk
    
    def Run(self): #método
        return True
    
class Bird(Animal): #classe filho
    def __init__(self, color, name, sound, walk, run):
        super().__init__(color, name, sound, walk, run) 

    def Fly(self): #método
        return True

class Dog(Animal): #classe filho
    def __init__(self, color, name, sound, walk, run):
        super().__init__(color, name, sound, walk, run)

    def Lick(self): #método
        return True

class Cat(Animal): #classe filho
    def __init__(self, color, name, sound, walk, run):
        super().__init__(color, name, sound, walk, run)

#bird = objeto
bird = Bird('Yellow', 'Parrot', 'PI PI', False, False) #instância da classe, objeto
print(bird.Sound())

#dog = objeto
dog = Dog('white', 'hana', 'AU AU', True, True) #instância da classe, objeto
print(dog.Lick())
