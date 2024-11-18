class Number:
  def add(self,a,b):
    result = a+b
    return result
  #function overloading 
  # Implementing same function with different functionality
  def add(self, a, b):
    res = a*b
    return res
  
  
obj = Number()    
print(obj.add(3,4))