import os 
import  mylist
import  myopp
import mytupple

if __name__=='__main__' :
 print('Wellcome To Python')
 print("Please Select  Your Subject :  \n1- Class Car \n2-Class Fruits : \n3- Polimorphism : \n4- List : \n5- Tupple :  ")
 option  = int(input())

 os.system('clear')
 if  option ==1 :
  bmw = myopp.Car("BMW") ;
  bmw.message()
  print("bmw Programmer is : %s "%bmw.programmer)
  print("Car Manufacturer is :  %s" %bmw.manufacturer)

#--------------------- Class  Fruits--------------------
 elif  option==2 :
  yellowbanana = myopp.Fruits("bababa")
  greenbanana  = myopp.Fruits("banana","Yazd GolKaneh")
  yellowbanana.message() 
  greenbanana.message()
  print("Owner of Golkhaneh is :  %s"%yellowbanana.getOwner())
 
  print('-------------------------------------------------------------------------------')
 elif  option== 3 : 
   pass

#-------------------------------Lists And  Tupple And Set------------------------------
 elif option==4 :
  mylist.declareList()

 elif  option==5 :
  mytupple.declareTupple()
