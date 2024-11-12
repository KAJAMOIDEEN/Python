class Car:
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def showData(self):
        print("My Car Info:",self.brand,self.model,self.color,self.year)


carObj = Car("Hyndai","breeza","red",2024)
nextCar = Car("Renault","Triber","Silver",2024)
nextCar.showData()
carObj.showData()
