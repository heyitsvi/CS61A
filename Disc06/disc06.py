# class Student:
    
#     max_slip_days = 3 # this is a class variable

#     def __init__(self, name, staff):
#         self.name = name # this is an instance variable
#         self.understanding = 0
#         staff.add_student(self)
#         print("Added", self.name)

#     def visit_office_hours(self, staff):
#         staff.assist(self)
#         print("Thanks, " + staff.name)

# class Professor:

#     def __init__(self, name):
#         self.name = name
#         self.students = {}

#     def add_student(self, student):
#         self.students[student.name] = student

#     def assist(self, student):
#         student.understanding += 1

#     def grant_more_slip_days(self, student, days):
#         student.max_slip_days = days

# class Button:
#     def __init__(self, pos, key):
#         self.pos = pos
#         self.key = key
#         self.times_pressed = 0

# class Keyboard:
#     """A Keyboard takes in an arbitrary amount of buttons, and has a
#     dictionary of positions as keys, and values as Buttons.
#     >>> b1 = Button(0, "H")
#     >>> b2 = Button(1, "I")
#     >>> k = Keyboard(b1, b2)
#     >>> k.buttons[0].key
#     'H'
#     >>> k.press(1)
#     'I'
#     >>> k.press(2) # No button at this position
#     ''
#     >>> k.typing([0, 1])
#     'HI'
#     >>> k.typing([1, 0])
#     'IH'
#     >>> b1.times_pressed
#     2
#     >>> b2.times_pressed
#     3
#     """
#     def __init__(self, *args):
#         self.buttons = {}
#         for button in args:
#             self.buttons[button.pos] = button

#     def press(self, info):
#         """Takes in a position of the button pressed, and
#         returns that button's output."""
#         try:
#             self.buttons[info].times_pressed += 1 
#             return self.buttons[info].key
#         except:
#             return ''

#     def typing(self, typing_input):
#         """Takes in a list of positions of buttons pressed, and
#         returns the total output."""
#         word = ''
#         for pos in typing_input:
#             word += self.press(pos)
#         return word

class Pet:
    
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')

# class Cat(Pet):
    
#     def __init__(self, name, owner, lives=9):
#         super().__init__(name, owner)
#         self.lives = lives

#     def talk(self):
#         """Print out a cat's greeting.

#         >>> Cat('Thomas', 'Tammy').talk()
#         Thomas says meow!
#         """
#         print(f'{self.name} says meow!')

#     def lose_life(self):
#         """Decrements a cat's life by 1. When lives reaches zero,
#         is_alive becomes False. If this is called after lives has
#         reached zero, print 'This cat has no more lives to lose.'
#         """
#         if self.lives > 0:
#             self.lives -= 1
#         else:
#             return 'This cat has no more lives to lose.'

import random as random
# from tkinter.font import names
# from unicodedata import name

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives


    # Insert other previously defined methods here

    

    @classmethod
    def adopt_random_cat(cls, owner):
        """
        Returns a new instance of a Cat with the given owner,
        a randomly chosen name and a random number of lives.
        >>> randcat = Cat.adopt_random_cat("Ifeoma")
        >>> isinstance(randcat, Cat)
        True
        >>> randcat.owner
        'Ifeoma'
        """
        names = ['Tom', 'Amelia','MeowMeow', 'Isabella', 'PawPaw']
        return cls(names[random.randint(0,len(names) - 1)], owner, random.randint(0,69))

# class NoisyCat(Cat):
#     """A Cat that repeats things twice."""
#     # def __init__(self, name, owner, lives=9):
#     #     # Is this method necessary? Why or why not?
#     #     "*** YOUR CODE HERE ***"

#     def talk(self):
#         """Talks twice as much as a regular cat.
#         >>> NoisyCat('Magic', 'James').talk()
#         Magic says meow!
#         Magic says meow!
#         """
#         for _ in range(2):
#             super().talk()

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret