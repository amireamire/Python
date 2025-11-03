class Car :
 programmer="amire.amir26@gmail.com" 
 manufacturer = ""

 def __init__(self,maker)  :
   self.manufacturer =maker
  
 def  message(self) :
  print("Wellcome To My Car")


 def carON(self) :
    print("Car is ON")

 def  carOFF(self) :
    print("Car is OFF")

#----------------------------------------------------- Another Class   Fruits---------------------------------

class  Fruits :
  family=""
  farmer =""
  __owner = ""
  def  __init__(self, family, farmer="Boshruyeh Golkhaneh")  :
    self.farmer = farmer 
    self.family  =family 
    if  (self.farmer=="Boshruyeh Golkhaneh") :
      self.color ="Yellow"
      __owner ="Hosssein Safari"
    else :
      self.color ="Green"
      __owner ="AnyBody"

  def message(self) :
    if (self.farmer=="Boshruyeh Golkhaneh")  :
     print("Manufactuer in Boshruyeh")
    else :
     print("Manufactur in Another Province")
     print("Color of Fruits is : %s " %self.color)
  def  getOwner(self) :
    return  self.__owner 
 
 
