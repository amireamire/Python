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
 print("Which Item  index Do You Want To Delete :  ")
 select=int(input()) ;
 programming.pop(select)
 print(programming)
