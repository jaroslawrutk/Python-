#Zadanie2




class D2:
  def __init__(self, punk1, punk2):
    self.punk1=punk1
    self.punk2=punk2
    
    
  def licz(self, other):
    d=((other.punk1-self.punk1)**2+(other.punk2-self.punk2)**2)**0.5
    return d
      
class D3(D2):
    def __init__(self, punk1, punk2, punk3):
      self.punk1=punk1
      self.punk2=punk2
      self.punk3=punk3
      
    def licz(self, other):
      d=((other.punk1-self.punk1)**2+(other.punk2-self.punk2)**2+(other.punk3-self.punk3)**2)**0.5
      return d
    
d2a=D2(0,0)
d2b=D2(2,2)
d3a=D3(0,0,0)
d3b=D3(2,2,2)




print(d2a.licz(d2b))
print(d3a.licz(d3b))
