#users
import pickle
ak=input("Enter Admin Key to authenticate :")
if(ak=="25"):
    f=open("users.dat","rb")
    print(["username","password","first name","last name","email","DOB","gender"])
    try:
        while True :
            s=pickle.load(f)
            print(s)
    except EOFError :
        pass
    f.close()
else:
    print("Contact admin for authorization")
