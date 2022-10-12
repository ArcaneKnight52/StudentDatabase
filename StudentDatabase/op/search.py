#search

#------------------------------------------------------------------------
#b)search by admmo
def AdmnoSearch_Stu():
    import pickle
    f=open("stu.dat","rb")
    key=input("Enter admission no. of student whose record is to be displayed : ")
    a=0
    while(a==0):
        if(len(key)==6 and key.isnumeric()):
            p=1
            break
        else:
            print("Please enter admission no. according to default font")
            key=input("Enter admission no. of student whose record is to be displayed : ")
            
            
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if(s[0]==key):
                print("RECORD FOUND."+"")
                print("-----------------------------------------------------------------------")
                print("The record of the student having admno",key,"is : ",s)
                flag=1
            else:
                pass
                
    except EOFError :
        pass
    if(flag==0):
        print("No such record exists with student admission no. being",key)
    print("-----------------------------------------------------------------------------")                
    f.close()
#---------------------------------------------
#a)search by name
def NameSearch_Stu():
    import pickle
    f=open("stu.dat","rb")
    key=input("Enter name of student whose record is to be displayed : ")
    b=0
    while(b==0):
        if(key.isspace()==False):
            for i in key:
                l=["!","@","#","$","%","^","&","*","(",")","=",">","<","?","/","|",",",""]
                allow=[" ",".","_","  ","-","'"]
                if(i not in l and i in allow and i.isnumeric()==False):
                    b+=1
                    break
                else:
                    print("Please enter name correctly")
                    key=input("Enter name of student whose record is to be displayed : ")
                           
    w=key.lower()
    flag=0
    cnt=0
    try:
        while True:
            s=pickle.load(f)
            if(s[1].lower()==w):
                print("RECORD FOUND.")
                print("-----------------------------------------------------------------")
                print("The record of the student",key,"is : ",s)
                flag=1
                cnt+=1
            else:
                pass
                
    except EOFError :
        pass
    if(flag==0):
        print("No such record exists with student name being",key)
        print("-----------------------------------------------------------------------------")
    elif(flag!=0 and cnt!=1):
        choice=input("There appears to be multiple records by same name. Would you like to search by admno.?? {yes/no}")
        if(choice in ("Y","y","YES","yes","Yes")):
            AdmnoSearch_Stu()

    f.close()
#-----------------------------------------------------------------
#menu for search
def Search_Menu():
    print("Enter the mode of searching..")
    print("------------------------------")
    print("a.Search by name")
    print("b.Search by admno")
    choice=input("Enter your choice (a/b) : ")
    k=0
    while(k==0):
        if(choice.lower()=="a"):
            NameSearch_Stu()
            k+=1
        elif(choice.lower()=="b"):
            AdmnoSearch_Stu()
            k+=1
        elif(choice.lower not in ("a","b")):
            print("Please retry with correct values!!")
            choice=input("Enter your choice (a/b) : ")

               







