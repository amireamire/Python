
import  myopp

if __name__=='__main__' :
 print('Wellcome To Python')
 bmw = myopp.Car("BMW") ;
 bmw.message()
 print("bmw Programmer is : %s "%bmw.programmer)
 print("Car Manufacturer is :  %s" %bmw.manufacturer)



#--------------------- Class  Fruits--------------------

 yellowbanana = myopp.Fruits("bababa")
 greenbanana  = myopp.Fruits("banana","Yazd GolKaneh")
 yellowbanana.message() 
 greenbanana.message()
 print("Owner of Golkhaneh is :  %s"%yellowbanana.getOwner())
 
 print('-------------------------------------------------------------------------------')
#polymorphism  class with same method
 for  x in  (yellowbanana,greenbanana,bmw) :
   x.message()
