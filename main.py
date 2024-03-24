class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old and I am {self.gender}.")


person1 = Person("Brian Kamana", 20, "male")
person1.introduce()