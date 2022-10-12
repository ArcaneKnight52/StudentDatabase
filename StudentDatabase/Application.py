#login
import signin, signup
print("\t\t ||Sign in to your account||")
print("-------------------------------------------------------")
print("a.Existing user")
print("b.New User")
choice=input("Enter your choice: [a or b] ")
if(choice.lower()=="a"):
    signin.SignIn()
elif(choice.lower()=="b"):
    signup.SignUp()
else:
    print("Invalid Choice!!")




    
