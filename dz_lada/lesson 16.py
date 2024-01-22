# Задания № 1

class Vehicle():
    def __init__(self,model,year):
        self.model = model
        self.year = year
        
    def Vehicle_model(self):
        print(f"Какая ваша модель транспортного средства ? {self.model} Какого она года ? {self.year}")
        

model_Vehicle = Vehicle('Лексус',2001)

model_Vehicle.Vehicle_model()

class Car (Vehicle):
    def __init__(self,fuel_type, model, year):
        super().__init__(model, year)
        self.fuel_type = fuel_type
        
    def car_new(self):
        print(f"Машина заправляется: {self.fuel_type} Модель машины: {self.model} Год машины: {self.year}")
        
car_lek = Car('бензином','Лексус',2001)
    
car_lek.car_new()
