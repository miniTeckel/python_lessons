class Animal:
    name = None
    age = None
    sex = None
    weight = None

    def __str__(self):
        if self.name is None:
            return '%s: "%s!"' %(self.__class__.__name__, self.speak())
        else:   
            return '%s %s: "%s!"' %(self.__class__.__name__, self.name, self.speak())

    def speak(self):
        pass


class Mammal(Animal):
    def __init__(self, name):
        self.name = name
    
    def give_milk(self):
        print("milk")

class Bird(Animal):
    def __init__(self, sex = "female"):
        self.sex = sex
    
    def lay_egg(self):
        print("12 eggs")

class Cow(Mammal):
    def speak(self):
        return "му-му"


class Pig(Mammal):
    def speak(self):
        return "хрю-хрю"


class Sheep(Mammal):
    def speak(self):
        return "бе-бе"


class Goat(Mammal):
    def speak(self):
        return "ме-ме"


class Goose(Bird):
    def speak(self):
        return "га-га"


class Chiken(Bird):
    def speak(self):
        if self.sex == "male":
            return "ку-ка-ре-ку"
        else: 
            return "ко-ко-ко"


class Duck(Bird):
    def speak(self):
        return "кря-кря"


if __name__ == "__main__":
    zorka = Cow("Звездочка")
    print(zorka)


    chiken = Chiken()
    print(chiken)
    print(Chiken("male"))