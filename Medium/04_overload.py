class Number:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    print("Constructor function")


  def add(self):
    result = self.a + self.b 
    return result
  #function overloading 
  # Implementing same function with different functionality
  def mul(self):
    res = self.a * self.b 
    return res
  
class Digit(Number):
  def __init__(self,a,b):
    super().__init__(a, b)

  def mul(self):
    print("Calling from from child class")
    return self.a * self.b 
   
  
obj = Number(4,5)
obj1 = Digit(2,2)
print(obj.mul())
print(obj1.mul())