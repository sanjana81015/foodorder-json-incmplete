
import json as js
class admin:

     def __init__ (self):
      self.fooditem={101:['dosa',1,200,0,25],102:['pizza',1,300,0,15]}

     def addfood(self):
        self.FoodID= len(self.fooditem) + 101

        name=input('enter food name : ')
        quantity=input('enter qty  : ')
        price=int(input('enter per plate price : '))
        discount=int(input('enter discount : '))
        stock=input('enter stock  : ')
        self.fooditem[self.FoodID]=[name,quantity,price,discount,stock]
        f=open('menu.json','w')
        js.dump(self.fooditem,f)
        f.close()
        print('food added successfully....')
        print(self.fooditem)

     def editfood(self):
        
        f=open('menu.json','r')
        data=js.load(f)
        
        food_id=input('enter food id  which u want to update')
        for i,k in data.items():
            if i==food_id:
                k[0] = input("Enter updated food name : ")
                k[1] = (input("Enter updated food quantity : "))
                k[2] = input("Enter updated food price : ")
                k[3] = input("Enter updated food discount : ")
                k[4] = (input("Enter updated food stock : "))
                f.close()
                f=open('menu.json','w')
                js.dump(data,f)
                f.close()
                f=open('menu.json','r')
                data=js.load(f)
                print(data)
                print('updated successfully')
                return
        print('pls check foodid and try again')

     def viewfood(self):
         f=open('menu.json','r')
         data=js.load(f)
         for i,j in data.items():
            print(f'food id : {i}\nName : {j[0]}\nQuantity : {j[1]} pieces\nPrice : {j[2]}rs\nDiscount : {j[3]}%\nStock : {j[4]} pieces available')
         f.close()

     def removefood(self):
        f=open('menu.json','r')
        data=js.load(f)
        food_id=input('enter food id  which u want to delete')
        for i,k in data.items():
            if i==food_id:
               f=open('menu.json','w')
               del data[i]
               js.dump(data,f)
               f.close()
               print('food item remove successfully')
               return
   
        print('check your ID and try again')
   
     def get(self):
      f=open('menu.json','r')
      data=js.load(f)

      for i,j in data.items():        
           print(f'Food ID: {i},{j[0]},{j[1]},{j[2]}per plate')
           f.close()
      return

     def getfood(self,fid):
         f=open('menu.json','r')
         data=js.load(f)
         
         for i,j in data.items():
           if fid==i:
              return j
         f.close()