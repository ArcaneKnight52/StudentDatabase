#cnt of stu:
def count_Stu():
    import pickle
    f=open("stu.dat","rb")
    cnt=0
    try:
        while True:
            d=pickle.load(f)
            cnt+=1
    except EOFError:
        pass
    print("The number of student records are : ",cnt)
    f.close()

