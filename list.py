def   defineList() :
 favo =['Programming','Sport','Linux','GIS']
 favo[1]="Sex"
 favo.append('Virualization')
 favo.insert(0,'GIS')
 print(favo)
 print("The Lenth of favo : %d"%len(favo))


 #define List With Constructor 

 programming =list(('c++','g++','perl','python') )
 print(programming)
 print(programming[0])
 package=list(('Iran Radiator','Bootan','Ferroli'))
 index=-1
 print(package[index])

 numbers=[]
 numbers.append([10,20,30,40,50,60,70,80,90,100])
 print(numbers)
 print(numbers[0])

 mylist=[[10,20,30] ,"C++","Python" , 2+2j]
 print(mylist)
 #---------------------define Nw List-------------------------------------
 flash =[2,4,8,16,32,64,128,256,512]
      #Flash 256-  512 G Rmov From List By Value And Index 
 flash.pop(7) 
 flash.remove(512) 
 print(flash)
       #Clear List  
 flash.clear()
 #-------------------------- Loop in Flash ------------------------------

 carmaker=['SAIPA' , 'IRAN Khodro' ,'Bahman']
 print(carmaker)
 for  maker  in carmaker :
   print(maker)

   #loop through  index 
 for  index  in  range (len(carmaker)) :
  print(carmaker[index])

#-------------------------------Copy Shallow Copy ------------------------
 fruits =['Banana','apple','strawberry','orange','apple']
 fruits.insert(0,'pear')
 fruits.append('kiwi')
 print(fruits)
 print(fruits.count('apple'))
 print("index of strawbery is :  %d "%fruits.index("strawberry"))
  # Delete item From  last  index
 fruits.pop()
 print(fruits)

# print('My First Favo = %s'%favo[0])
 
 
 
