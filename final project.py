import pandas as pd
from pandas import Series, DataFrame
df = pd.read_excel (r'D:\WORK\CSE project\Book1.xlsx')
def student_data():
    data1 = { 'Name' : [name], 'RollNo' : [rollno], 'Email' : [email], 'D.O.B' : [DOB], 'Course' : [course], 'Gender' : [gender]}
    df1 = DataFrame(data1)
    df = df.append(df1)

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Quit")
    n2=int(input("Enter your choice: "))
    if n2==1:
           add_student()
    if n2==2:
        view_student()
    if n2==3:
        update_student()
    if n2==4:
        delete_student()
    if n2==5:
        Quit()
def add_student():
    writer = pd.ExcelWriter('Book1.xlsx', engine='xlsxwriter')
    writer.save()
    name = input("enter name: ")
    rollno = input("enter rollno: ")
    email = input("enter email: ")
    DOB = input("Enter Date of Birth: ")
    course = input("Enter Course: ")
    gender = input("Enter Gender: ")
    student_data
    input("\n Press any key to continue")
    return display_menu()

def view_student():
    
    rollno = input("Enter Roll No.: ")
    print(df.loc[df['RollNo'] == rollno])
    input("\n Press any key to continue")
    
    return display_menu()
def update_student():
    
    writer = pd.ExcelWriter('Book1.xlsx', engine='xlsxwriter')
    writer.save()
    #Changing Name
    name = input("Enter new name: ")
    df.loc[df['RollNo'] == rollno, 'Name'] = name
    
#Changing Email
    email = input("Enter new email: ")
    df.loc[df['RollNo'] == rollno, 'Email'] = email

#Changing D.O.B
    DOB = input("Enter new Date of Birth: ")
    df.loc[df['RollNo'] == rollno, 'D.O.B'] = DOB

#Changing Course
    course = input("Enter new course: ")
    df.loc[df['RollNo'] == rollno, 'Course'] = course
    input("\n Press any key to continue")
    student_data
    return display_menu()
def fun():
    pass
with open('students.txt','r') as f:
    lines=f.read()
    n=input("Enter password: ")
    if n==lines:
        display_menu()
        fun()

               
       
       

