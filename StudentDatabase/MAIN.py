
#main programm of mini project
def MainPage():
    from op import add, read, search, export, count, update, delete
    while True:
        print("\t\t ||Welcome to StudentDatabase mini_Project||  VERSION 1.0")
        print("--------------------------------------------------------")
        print("MENU:")
        print("1. To add details of new student.")
        print("2. To display all student details.")
        print("3. To search the record of the student.")
        print("4. To export student details to a text file.")
        print("5. To count the no. of student records in database.")
        print("6. To update details of a student.")
        print("7. To delete the entry of a student.")
        print("--------------------------------------------------------")
        print("Enter your choice: (at next line)")
        choice=int(input())
        if(choice==1):
            add.AdmnoCheckAdd_Stu()
        elif(choice==2):
            read.Read_Stu()
        elif(choice==3):
            search.Search_Menu()
        elif(choice==4):
            export.Export_Menu()
        elif(choice==5):
            count.count_Stu()
        elif(choice==6):
            update.Update_Stu()
        elif(choice==7):
            delete.Delete_Stu()
        check=input("Do you want to return to main menu? {Yes/No}  : ")
                    
        if(check not in("Y","y","YES","yes","Yes")):
            break

                
                
            
    print("Thank you for your valuable time at Student_Database :-). \nWe hope you have a wonderful day ahead")

        

