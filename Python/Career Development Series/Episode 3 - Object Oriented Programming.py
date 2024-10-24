# Creating classes

class person:
    pass
    
# Creating an object

class person:
    pass
Daniel = person

# Adding some attributes

class person:
    def __init__(self, age, sport):
        self.age = age
        self.sport = sport

Daniel = person('22', 'football')

# Printing these attributes

print (Daniel.age)

Daniel = person('22', 'football')
James = person('40', 'tennis')
print (Daniel.age)
print (James.sport)

# Methods in a class

class person:
    def __init__(self, age, sport):
        self.age = age
        self.sport = sport
    
    def changeSport(self, newSport):
        self.sport = newSport

Daniel = person('22', 'football')

Daniel.changeSport('cricket')
print (Daniel.sport)

# Starting with inheritance
# Superclasses and subclasses

class sup:
    def example1(self):
        print ('I am in the super class')
    
class sub(sup):
    def example2(self):
        print ('I am in the sub class')
    
class1 = sub()
class1.example2()
class1.example1()



class sup:
    def example1(self):
        print ('I am in the super class')
    
class sub(sup):
    def example1(self):
        print ('I am in the sub class')
    
class1 = sub()
class1.example1()

# Multiple inheritance

class sup_1:
    def example1(self):
        print ('I am in the first super class')

class sup_2:
    def example2(self):
        print ('I am in the second super class')

class sup_3:
    def example3(self):
        print ('I am in the third super class')

class sub(sup_1,sup_2,sup_3):
    def example4(self):
        print ('I am in the sub class')
    
class1 = sub()
class1.example1()
class1.example2()
class1.example3()
class1.example4()

# The super() function

class sup:
    def example1(self):
        print ('I am in the super class')
    
class sub(sup):
    def example1(self):
        print ('I am in the sub class')
        super().example1()
    
class1 = sub()
class1.example1()

# Multiple super classes with the super() function

class sup_1:
    def example1(self):
        print ('I am in the first super class')

class sup_2:
    def example1(self):
        print ('I am in the second super class')

class sup_3:
    def example3(self):
        print ('I am in the third super class')

class sub(sup_1,sup_2,sup_3):
    def example4(self):
        print ('I am in the sub class')
        super().example1()
        super().example3()

class1 = sub()
class1.example4()

# Encapsulation
# Protected member is one underscore, _
# Private member is two underscores, __

class sup: 
    def __init__(self): 
        self._a = "Protected Member"
        self.__b = "Private Member"
  
class sub(sup): 
    def __init__(self):
        super().__init__() 
        print (self._a)
        #print (self.__b)
  
example1 = sub() 

# Real world use of encapsulation

class private:
    def __init__(self, attempt):
        self.attempt = attempt
        self.__password = 'Hello123'
        if self.__password == attempt:
            print ('Password is correct')
        else:
            print ('Password is incorrect')
attempt1 = private('Hello134')
attempt2 = private('Hello123')
print (attempt2.attempt)
#print (attempt1.__password)

# Polymorphism

class vehicles:
    def __init__(self, seats, wheels):
        self.seats = seats
        self.wheels = wheels
class car(vehicles):
    def __init__(self, passengers,seats, wheels):
        super().__init__(seats, wheels)
        self.passengers = passengers
class bus(vehicles):
    def __init__(self, capacity,seats, wheels):
        super().__init__(seats, wheels)
        self.capacity = capacity
class lorry(vehicles):
    def __init__(self, load, seats, wheels):
        super().__init__(seats, wheels)
        self.load = load

example1 = bus(100, 101, 8)
example2 = car(4, 5,4)
example3 = lorry(3000, 2, 8)
