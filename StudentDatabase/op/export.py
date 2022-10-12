#to export
#-----------------------------------------------------------------------
#b)specific records
def ExportSpecific_Stu():
    import pickle
    f=open("stu.dat","rb+")
    fn=open("Export_stu_details.txt","w")
    w=input("Enter admno. of student whose record is to be exported : ")
    flag=0
    try:
        while True:
            l=pickle.load(f)
            if(l[0]==w): 
                fn.write("\t\t || Details of "+l[1]+"||")
                fn.write("\n"+"=========================================================")
                fn.write("\n"+"admno : "+l[0]+"\n")
                fn.write("name : "+l[1]+"\n")
                fn.write("class : "+l[2]+"\n")
                fn.write("sec : "+l[3]+"\n")
                fn.write("gender : "+l[4]+"\n")
                fn.write("stream : "+l[5]+"\n")
                fn.write("phone : "+l[6]+"\n")
                fn.write("----------------------------------------------------------")
                flag=1    
            else:
                pass
    except EOFError:
        pass
    if(flag==0):
        print("NO such record having admno",w)
    elif(flag==1):
        print("Record exported succesfully!")
    print("---------------------------------------------------------------------------")
    f.close()
    fn.close()
#---------------------------------------------------------------
#a)export all stu

def ExportAll_Stu():
    import pickle
    f=open("stu.dat","rb")
    fn=open("exported_stu_details.txt","w")
    flag=0
    fn.write("=========================================================")
    try:
        while True:
            l=pickle.load(f)
            fn.write("\n"+"admno : "+l[0]+"\n")
            fn.write("name : "+l[1]+"\n")
            fn.write("class : "+l[2]+"\n")
            fn.write("sec : "+l[3]+"\n")
            fn.write("gender : "+l[4]+"\n")
            fn.write("stream : "+l[5]+"\n")
            fn.write("phone : "+l[6]+"\n")
            fn.write("----------------------------------------------------------")
            flag=1
    except EOFError:
        pass
    if(flag==1):
        print("Succesfully exported details of all student records.")
        print("The records of all the students has been exported to file: exported_stu_details")
    f.close()
    fn.close()

#-------------------------------------------------------

#Export menu
def Export_Menu():
    print("Enter the mode of exporting..")
    print("------------------------------")
    print("a.export all details")
    print("b.export details of specific student")
    choice=input("Enter your choice (a/b) : ")
    k=0
    while(k==0):
        if(choice.lower()=="a"):
            ExportAll_Stu()
            k+=1
        elif(choice.lower()=="b"):
            ExportSpecific_Stu()
            k+=1
        elif(choice.lower() not in ("a","b")):
            print("Please retry with correct values!!")
            choice=input("Enter your choice (a/b) : ")


              
        
        
        






