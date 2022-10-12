#sign up
def SignUp():
     import pickle, random, signin, os
     f=open("users.dat","ab+")
     print("Are you")
     print("A.new user")
     print("b.Registered user")
     choice=input("Enter your choice (a/b) : ")
     if(choice.lower()=="a"):
          print("**********************************************************")
          print("\t\t ||REGISTRATION FORUM||")
          print("=======================================================")
          fn=input("Enter your first name : ")
          l=input("Enter your last name : ")
          email=input("Enter your email : ")
          d=input("Enter DOB : ")
          g=input("Enter gender : ")
          r=str(random.randint(100,999))
          u=fn+r
          print(u,"This will be used as your username")
          p=input("Create strong password : ")
          cp=input("Confirm password : ")
          if(p!=cp):
               print("Password did not match")
               print("try again")
          else:
               print("Congrats")
               print("Registrattion Succesful!!")
               
          kp=[u,p,fn,l,email,d,g]
          pickle.dump(kp,f)
          
     elif(choice.lower()=="b"):
          signin.SignIn()
     else:
          print("Invalid choice!!")
     f.close()
                             
     
