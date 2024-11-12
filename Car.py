class Car:
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def __str__(self):
        return f"Brand:{self.brand} \nModel{self.model} \nColor:{self.color} \nYear:{self.year}"


carObj = Car("Hyndai","breeza","red",2024)
print(carObj)
