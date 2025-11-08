def  declareList()   :
 favo = [10,20,30,40,50,'gis','remote sensing','sport']
 favo.append('programming')
 favo.insert(5,'virtualization')
 print(favo)

 print("Which  List item do you want to delete ? : ")
 parameter =input()
 favo.remove (parameter)
 print(favo)

 print("Are You Sure To Delete All List : ")
 select= input()
 if  select =='yes' or  'y' :
  favo.clear()
 print(favo)

 #remove item by index 
 programming = ['c','c++','python','java','C#' ,'go']
 print(programming)
 print("Which Item  index Do You Want To Delete :  ")
 select=int(input()) ;
 programming.pop(select)
 print(programming)
 print('-------------------Slicing List ----------------------------')

 myfruits=['banana','onion','potato','coconut','pear','kiwi','cherry','apple','orange','pomegranate']
 print(myfruits)
 print(myfruits[0:1])
 print(myfruits[1:])
 print(myfruits[:5])

 print('-----------------------Expand List-------------------------------')
 practice1=['c++','python','c']
 practice2=['MySQL','SQL Server','Oracleee']
 practice1.extend(practice2) ;
 print(practice1)
