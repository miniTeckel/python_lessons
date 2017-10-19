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


class Cow(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "му-му"


class Pig(Animal):
    def __init__(self, name):
        self.name = name


    def speak(self):
        return "хрю-хрю"


class Sheep(Animal):
    def __init__(self, name):
        self.name = name


    def speak(self):
        return "бе-бе"


class Goat(Animal):
    def __init__(self, name):
        self.name = name


    def speak(self):
        return "ме-ме"


class Goose(Animal):
    def speak(self):
        return "га-га"


class Chiken(Animal):
    def __init__(self, sex = "female"):
        self.sex = sex

    def speak(self):
        if self.sex == "male":
            return "ку-ка-ре-ку"
        else: 
            return "ко-ко-ко"


class Duck(Animal):
    def speak(self):
        return "кря-кря"


if __name__ == "__main__":
    zorka = Cow("Звездочка")
    print(zorka)


    chiken = Chiken()
    print(chiken)
    print(Chiken("male"))