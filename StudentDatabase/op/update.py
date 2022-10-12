#=====================================================================================                   
#update
def Update_Stu() :
    pwd=input("Enter pwd to authenticate:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        key=input("Enter admission no. of student whose record is to be updated : ")
        print("=====================================================================")
        import pickle
        f=open("stu.dat","rb")
        temp=open("temp.dat","wb")
        x=False
        try:
            while True:
                s=pickle.load(f)
                if(s[0]==key):
                    l=[]
                    print("Enter the new details which are to be updated for student",s[1])
                    n=input("Enter name of student( format:KP_Sriram) : "+" ")
                    c=input("Enter class of student which is to be updated: "+" ")
                    sec=input("Enter section of student which is to be updated: "+" ")
                    g=input("Enter gender of student {Male/Female}which is to be updated: "+" ")
                    st=input("Enter stream of student which is to be updated: "+" ")
                    pn=input("Enter phone number of student which is to be updated: "+" ")
                    l=[key,n,c,sec,g,st,pn]
                    x=True
                    pickle.dump(l,temp)
                    
                else:
                    pickle.dump(s,temp)
        except EOFError :
            pass
        
        if(x==False):
            print("No such record exists having admno",key)
            print("=================================================================")
            f.close()
            temp.close()
        elif(x==True):
            f.close()
            temp.close()
            import os
            os.remove("stu.dat")
            os.rename("temp.dat","stu.dat")
            print("Updated succesfully!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Not authorized to update the contents of stu_records.To Gain authorization contact admin!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

