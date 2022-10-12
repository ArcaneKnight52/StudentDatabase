#to add new stu
def Add_Stu():
    """accepts information and adds them into file."""
    import mysql.connector as v
    con=v.connect(host="localhost",user="root",password="root",database="LibraryOg")
    cur=con.cursor()
    pwd=input("Enter the password to authenticate into the database:")
    print("Authenticating....")
    print(".")
    print(".")
    print(".")
    if(pwd=="Mukesh_Bohra" or pwd=="ak"):
        a=int(input("Enter book id:"))
        sql="insert into books(book_id) values(%s)"
        values=(428)
        print(a)
        cur.execute(sql,values)
        con.commit()
        print(cur.rowcount,"row inserted")
        """b=input("Enter name of the book")
        c=input("Enter the author of the book")
        d=input("Enter section of student : "+" ")
        e=input("Enter price of the book ")
        f=input("Enter the id of the issuer: ")
        
                        
        l=[a,n,c,sec,g,st,pn]"""
        
        print("Student details added.")
        print("Thank you for your valued contribution!")
          
    else:
        print("Sorry, your password is wrong hence you cannot be authenticated. Contact admin for authorization.")
    con.close()

#====================================
"""
def AdmnoCheckAdd_Stu():
    import pickle
    f=open("stu.dat","rb")
    key=input("Enter admission no. of student whose record is to be added : ")
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if(s[0]!=key):
                Add_Stu()
                flag=1
                break
            else:
                print("There already exists a record with student admission no. being",key)
                break
                
    except EOFError :
        pass
        
    print("-----------------------------------------------------------------------------")
    f.close()
"""

    
