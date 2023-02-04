
from admin import admin
from user import user
class main_admin:
    def execute (self,choice):
        if choice==1:
         print('______ADD FOOD ITEM______')
         adminobj.addfood()
        elif choice==2:
         print('______EDIT FOOD DETAILS______')
         adminobj.editfood()
        elif choice==3:
         print('______VIEW ALL FOOD ITEMS______')
         adminobj.viewfood() 
        elif choice==4:
         print('______REMOVE A FOOD ITEM______')
         adminobj.removefood() 
       
        
class main_user:
     def u_exe(self,choice):
       if choice==1:
         print('______register______')
         userobj.register()
         print('_____login______')
         userobj.login()

       if choice==2:
         print('_____login______')
         userobj.login()
if __name__=='__main__':
   obj=main_admin()
  
   obj1=main_user()
  


   print("1.Admin\n2.user")
  
   ch=int(input("Enter your choice  :  "))
   if ch==1:
        adminobj=admin() 
       
        print('..................you are welcome to admin portal....................')
        c=0
        while c!='N':
          ch1=int(input('1.ADD FOOD ITEMS\n2.EDIT FOOD ITEMS USING FOODID\n3.VIEW THE LIST OF ALL FOOD ITEMS\n4.REMOVE A FOOD ITEM FROM THE MENU USING FOODID\n5.EXIT'))
          if ch1==5:
            c='N'
            print('thank you, you are exit now')
           
          obj.execute(ch1)
   if ch==2:
      print('..................hello user....................')
      userobj=user()

      while True:
        ch2=int(input("Enter your choice  :  \n1.Register\n2.Log in to the application"))
        obj1.u_exe(ch2)
