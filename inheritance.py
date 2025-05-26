class Animal:
    def speak(self):
        print('Animal makes sound')
class Cat(Animal):
    def sound(self):
        print('cat makes sound moew')
        
cat1 = Cat()  
cat1.speak()     
cat1.sound()

#example 2

class Father:
    def skills(self):
        print('fishing')
        
class Mother:
    def skills(self):
        print('cooking')
        
class child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)

c = child()
c.skills()

#polymorphism
class Bird:
    def fly(self):
        print('birds fly in the sky')
        
class Eagle(Bird):
    def fly(self):
        print('eagle flies at high altitude') 
        
class Sparrow(Bird):
    def fly(self):
        print('sparrow flies at low altitude')       

def flight_test(bird):
    bird.fly()
#objects    
eagle1 = Eagle()
sparrow1 = Sparrow()   

flight_test(eagle1)
flight_test(sparrow1)
