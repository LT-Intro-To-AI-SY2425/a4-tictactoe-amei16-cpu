# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n = "no name", a = 0):
        self.name = n
        self.age = a

    def __str__(self) -> str:
        if self.age == 1:
            s = f"{self.name} is {self.age} year old"
        else:
            s = f"{self.name} is {self.age} years old"
        return s


logan = Dog("logan", 8)
cookie = Dog()
maple = Dog("maple", 1)

print(logan.name)
print(cookie)
print(maple)
