#delete
def Delete_Stu() :
    pwd=input("Enter pwd to authenticate:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        key=input("Enter admission no. of student whose record is to be deleted : ")
        print("====================================================================")
        import pickle
        f=open("stu.dat","rb")
        temp=open("temp.dat","wb")
        k=False
        try:
            while True:
                s=pickle.load(f)
                if(s[0]==key):
                    k=True
                else:
                    pickle.dump(s,temp)
        except EOFError :
            pass
        
        if(k==False):
            print("No such record exists having admno",key)
            print("-----------------------------------------------------------------")
            f.close()
            temp.close()
        
        elif(k==True):
            f.close()
            temp.close()
            import os
            os.remove("stu.dat")
            os.rename("temp.dat","stu.dat")
            print("Deleted succesfully!!!")
            print("==================================================================")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Not authorized to update the contents of stu_records.To Gain authorization contact admin!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

