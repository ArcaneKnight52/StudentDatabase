#signup
def SignIn():
    import MAIN, pickle, os
    f=open("users.dat","rb")
    um=input("Enter username : ")
    p=input("Enter password : ")
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if(s[0]==um and p==s[1]):
                print("Sign In Succesful!!")
                print("Opening main page...")
                MAIN.MainPage()
                flag=1
    except EOFError :
        pass
    if(flag!=1):
        print("Invalid Credentials")
    
    f.close()
    os.system("cls")   
