class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

def play_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()
play_sound(dog)  # Output: Woof!
play_sound(cat)  # Output: Meow!
play_sound(cow)  # Output: Moo!