

# class for car 


class Car:
    def __init__(self,brand : str,model : str)->None:
        self.brand = brand
        self.model = model
        
    def displayCar(self)->str:
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,batterySize : str, brand, model)->None:
        # function "super()."  to inherit all the class variables 
        super().__init__(brand,model)
        self.batterySize = batterySize
        
        
toyotta = Car("corolla","2015");

cyberTruck = ElectricCar("tesla", "2026", "120KW")

print(cyberTruck.displayCar())


# print(toyotta.brand)
# print(toyotta.model)
# print(toyotta.displayCar())
        
         