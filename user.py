import json as js
from admin import admin
class user():
    def __init__(self):
      self.user_data = {}
      self.order_history = []
      self.adminobj=admin()

    def register(self):
          user_id = len(self.user_data) + 1
        
          full_name=input("Enter the full name :    ")
          phone_no=input("Enter the mobile no  :   ")
          email=input("Enter the email  :   ")
          address=input("Enter the address  :   ")
          password=input("Enter the password  :   ")

         
          self.user_data[user_id] = [full_name, phone_no, email,address,password]
          f=open('userdata.json','w')
          js.dump(self.user_data,f)
          f.close()
          f=open('userdata.json','r')
          data=js.load(f)
          for i,j in data.items():
           print(f'welcome {j[0]} you have registered eith id {i} successfully.. ')
          f.close()
         

    def login(self):
         Email=input("Enter the email  :   ")
         Password=input("Enter the password  :   ")
         f=open('userdata.json','r')
         data=js.load(f)
         for i, j in data.items():
            if j[2] == Email and j[3] == Password:
                    print(f"Welcome {j[0]}! You are now logged in.")
                    while True:
                        print("1. Place new order")
                        print("2. Order history")
                        print("3. Update profile")
                        print("4. Log out")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                              self.place_order()
      
                        elif choice == 2:
                              self.view_history()
                        elif choice == 3:
                              self.update_profile()
                        elif choice == 4:
                              print("Logged out successfully")
                        
                              return
                  
            else:
                  print("Invalid email or password")   
    def place_order(self):
        print("Available food items:")
        self.adminobj.get()
        food_id = input("Enter the ID of the food item you want to order: ")
        quantity = int(input("Enter the quantity you want to order: "))
        food_item = self.adminobj.getfood(food_id)
        if food_item:
            food_name = food_item[0]
            price = food_item[2]
            discount = food_item[3]
            Stock = food_item[4]
            total_price = (price * quantity)- ((discount/100)*(price*quantity))
            if quantity>Stock:
                        print(f'now we have only {food_item[4]} pieces')
        
            if quantity<=Stock:
                  self.order_history.append((food_id, food_name, quantity, total_price))

                  f=open('orderhis.json','w')
                  print(f"Your order for {quantity} {food_name} of amount {total_price }Rs has been placed .")
                  food_item[4] = Stock-quantity
                  f=open('orderhis.json','w')
                  js.dump(self.order_history,f)
                  for i,j in self.user_data.items():
                   print(f'THANK YOU......{j[0]}')
                  
            
        else:
            print("Invalid food ID. Please try again.")

    def view_history(self):
      f=open('orderhis.json','r')
      data=js.load(f)
      for i in data:
       print(f'food id : {i[0]}\nfood name : {i[1]}\nquantity : {i[2]}\nprice : {i[3]}')


    def update_profile(self):
      f=open('userdata.json','r')
      data=js.load(f)
      for i,j in data.items():
        print(f'USER ID : {i}\nFULL NAME : {j[0]}\nMOBILE NO : {j[1]}\nEMAIL ID : {j[2]}\nADDRESS : {j[3]}')
      f.close()
      up=input('do you want your profile ? if yes then press y ')
      if up=='y':
            f=open('userdata.json','r')
            data=js.load(f)
            for i,j in data.items():
            
                  j[0]=input('enter updated name : ')
                  j[1]=input('enter updated mobile number : ')
                  j[3]=input('enter updated address : ')
                  f=open('userdata.json','w')
                  js.dump(data,f)
                  f.close()
            print('you have successfully updated your profile : ')