class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


class student(Person):
  def sum(self,a,b):
    print("sum is",a+b)

x = student("John", "Doe")
x.printname()
x.sum(90,80)