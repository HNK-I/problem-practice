# ? 1- error occuring related to display function for electric car as model is unable to be rendered!!
# ? 2- 2nd error is occuring related to get_brand() function as interpreter is not recognizing it as attribute!!
#--------------------------------------------------------------------------------------------------------------------------
# ! 1- try to implement encapsulation in JS and TS and cpp....
#--------------------------------------------------------------------------------------------------------------------------
# -> 1- Now practicing polymorphism , in simple terms it's variation between classes that overlaps in terms of attributes and methods...


class Car:
    def __init__(self,brand : str,model : str):
#       Attributes

        self.model = model
#       private attribute brand!!
        self.__brand = brand
#      Methods

#       Getter function for private attribute brand
    def get_brand(self):
        return self.__brand

        
    def displayCar(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,batterySize, brand, model)->None:
        # function "super()."  to inherit all the class variables 
        super().__init__(brand,model)
        self.batterySize = batterySize
        
    def displayCar(self)->str:
        return f"{self.get_brand()} {self.batterySize} {self.model}"
        
toyotta = Car("corolla","2015");

cyberTruck = ElectricCar("239kw", "tesla", "s")

print(cyberTruck.displayCar())

print(cyberTruck.get_brand())


# print(toyotta.brand)
# print(toyotta.model)
# print(toyotta.displayCar())
        
         