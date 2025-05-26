from abc import ABC,abstractmethod
class   Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    
    def go(self):
        print('you drive the car') 
    def stop(self):
        print('you stop the car')
        
class   Motocycle(Vehicle):
    
      def go(self):
        print('you ride the motorcycle')
      def stop(self):
        print('you stop the motorcycle')
    
motorcycle = Motocycle()
motorcycle.go()
motorcycle.stop()