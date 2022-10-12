#to read stu
def ReadForUser_Stu():
    import pickle
    f=open("stu.dat","rb")
    
    try:
        while True:
            s=pickle.load(f)
            print("-----------------------------------------------------------------------------")
            print("\t\t || Details of "+s[1]+"||")
            print("\n"+"=========================================================")
            print("\n"+"admno : "+s[0]+"\n")
            print("name : "+s[1]+"\n")
            print("class : "+s[2]+"\n")
            print("sec : "+s[3]+"\n")
            print("gender : "+s[4]+"\n")
            print("stream : "+s[5]+"\n")
            print("phone : "+s[6]+"\n")
            print("----------------------------------------------------------")
            

    except EOFError:
        pass
    
            
    print("-----------------------------------------------------------------------------")
    f.close()
#========================================================
def ReadForcoAdmin_Stu():
    import pickle
    f=open("stu.dat","rb")
    
    try:
        while True:
            s=pickle.load(f)
            print(s)
            

    except EOFError:
        pass
    
            
    print("-----------------------------------------------------------------------------")
    f.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def Read_Stu():
    print("Enter the mode of viewing..")
    print("------------------------------")
    print("a.View Elaboratly")
    print("b.View Technically")
    p=0
    choice=input("Enter your choice (a/b) : ")
    while(p==0):
        if(choice.lower()=="a"):
            ReadForUser_Stu()
            p+=1
        elif(choice.lower()=="b"):
            ReadForcoAdmin_Stu()
            p+=1
        else:
            print("Please enter correct values!!!!!")
            choice=input("Enter your choice (a/b) : ")
            


