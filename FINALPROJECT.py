
import pandas as pd
from pandas import Series, DataFrame

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Update Attendance")
    print("6. Quit")
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
        attendance()
    if n2==6:
        print("Thanks for using our system")
        
        
def add_student():
    
    name = input("Enter Name: ")
    #validating Name
    while(name.isalpha() == False or len(name) < 2):
        name = input("Please enter a valid Name: ")
    
    rollno = input("Enter Rollno.: ")
    #Validating RollNo
    while(len(rollno) != 9 or rollno[:2] != "AU"):
        rollno = input("Please enter a valid RollNo.(AUXXXXXXX): ")
    
    
    email = input("Enter Email: ")
    #Validating Email
    while ("@ahduni.edu.in" not in email):
        email = input("Please enter valid Ahmedabad Eniversity Email: ")
        
    DOB = input("Enter Date of Birth (DD/MM/YY): ")
    #Validating DOB format
    import datetime

    day,month,year = DOB.split('/')

    isValidDate = True
    try :
        datetime.datetime(int(day), int(month), int(year))
    
    except ValueError :
        isValidDate = False

    while (isValidDate == False):
        DOB = input("Please enter valid format for Date of Birth (DD/MM/YY): ")
        day,month,year = DOB.split('/')
        isValidDate = True
        try :
            datetime.datetime(int(day), int(month), int(year))
    
        except ValueError :
            isValidDate = False

    course = input("Enter Course: ")
    
    gender = input("Enter Gender: ")
    #Validating gender
    while(gender != 'M' and gender != 'F'):
        gender = input("Please enter valid input (M/F): ")

    decision = input("Enter Y to add attendance or N to skip: ")
    
    if decision == "Y":
        df = pd.read_excel(r'Student data.xlsx')
        total = int(input("Enter total number of lectures: "))
        attended = int(input("Enter number of lectures attended: "))

        while(total < attended):
            total = int(input("Please enter valid number of total lectures: "))
            attended = int(input("Please enter valid number of attended lectures: "))

        perc = (attended/total)*100
        percent = round(perc, 2)
        data1 = { 'Name' : [name], 'RollNo' : [rollno], 'Email' : [email], 'D.O.B' : [DOB], 'Course' : [course], 'Gender' : [gender], 'Attendance(%)' : [percent] }
        df1 = DataFrame(data1)
        df = df.append(df1)

        print(df.loc[df['RollNo'] == rollno])

        writer = pd.ExcelWriter('Student data.xlsx', engine='xlsxwriter')

        df.to_excel(writer, sheet_name='Sheet1', index=False)

        writer.save()

        n3=input("Enter Y to add another student or N to return to Main Menu: ")
        
        while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to add another student or N to return to Main Menu: ")
            
        if n3 =='N':
            return display_menu()
        elif n3 =='Y':
            return add_student()
            

    if decision == "N":
        df = pd.read_excel(r'Student data.xlsx')
        data1 = { 'Name' : [name], 'RollNo' : [rollno], 'Email' : [email], 'D.O.B' : [DOB], 'Course' : [course], 'Gender' : [gender]}
        df1 = DataFrame(data1)
        df = df.append(df1)

        print(df.loc[df['RollNo'] == rollno])

        writer = pd.ExcelWriter('Student Data.xlsx', engine='xlsxwriter')

        df.to_excel(writer, sheet_name='Sheet1', index=False)

        writer.save()

        n3=input("Enter Y to add another student or N to return to Main Menu: ")
        
        while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to add another student or N to return to Main Menu: ")
            
        if n3 =='N':
            return display_menu()
        elif n3 =='Y':
            return add_student()
    
def view_student():
    df = pd.read_excel(r'Student data.xlsx')
    rollno = input("Enter Roll No.: ")

    print("\n")
    print(df.loc[df['RollNo'] == rollno])

    print("\n")
    n3=input("Enter Y to view another student or N to return to Main Menu: ")
    
    while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to view another student or N to return to Main Menu: ")
            
    if n3 =='N':
        return display_menu()
    elif n3 =='Y':
        return view_student()

def update_student():

    df = pd.read_excel(r'Student data.xlsx')
    rollno = input("Enter Roll No.: ")
    
    print("What would you like to change")
    print("1. Name")
    print("2. Email")
    print("3. D.O.B")
    print("4. Course")
    n1=int(input("Enter your choice: "))
    if n1==1:
        #Changing Name
        name = input("Enter new name: ")
        while(name.isalpha() == False or len(name) < 2):
            name = input("Please enter a valid name: ")
        df.loc[df['RollNo'] == rollno, 'Name'] = name
        
    elif n1==2:
        #Changing Email
        email = input("Enter new email: ")
        while ("@ahduni.edu.in" not in email):
            email = input("Please enter valid email: ")
        df.loc[df['RollNo'] == rollno, 'Email'] = email
       
    elif n1==3:
        #Changing D.O.B
        DOB = input("Enter new Date of Birth: ")
        import datetime

        day,month,year = DOB.split('/')

        isValidDate = True
        try :
            datetime.datetime(int(day), int(month), int(year))
    
        except ValueError :
            isValidDate = False

        while (isValidDate == False):
            DOB = input("Please enter valid format for Date of Birth (DD/MM/YY): ")
            day,month,year = DOB.split('/')
            isValidDate = True
            try :
                datetime.datetime(int(day), int(month), int(year))
    
            except ValueError :
                isValidDate = False

    
        df.loc[df['RollNo'] == rollno, 'D.O.B'] = DOB
           
    elif n1==4:
        #Changing Course
        course = input("Enter new course: ")
        df.loc[df['RollNo'] == rollno, 'Course'] = course

    print("Student record updated \n")

    print(df.loc[df['RollNo'] == rollno])
    print("\n")

    writer = pd.ExcelWriter('Student data.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()
    
    n3=input("Enter Y to update another student record or N to return to Main Menu: ")
    
    while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to update another student record or N to return to Main Menu: ")
            
    if n3 =='N':
        return display_menu()
    elif n3 =='Y':
        return update_student()
    

def attendance():
    df = pd.read_excel(r'Student data.xlsx')

    rollno = input("Enter Roll No.: ")

    total = int(input("Enter total number of lectures: "))
    attended = int(input("Enter number of lectures attended: "))
    print("\n")
    
    perc = (attended/total)*100
    percent = round(perc, 2)
    df.loc[df['RollNo'] == rollno, 'Attendance(%)'] = percent

    print(df.loc[df['RollNo'] == rollno])
    
    writer = pd.ExcelWriter('Student data.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()
    
    n3=input("\n Enter Y to view attendance of another student or N to return to Main Menu: ")

    while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to view attendance of another student or N to return to Main Menu: ")
            
    if n3 =='N':
        return display_menu()
    
    elif n3 =='Y':
        return attendance()


def delete_student():
    df = pd.read_excel(r'Student data.xlsx')
    
    rollno = input("Enter Roll No.: \n")

    df = df.set_index(df.RollNo)
    df = df.drop(rollno)
 
    print("Student record deleted \n")

    writer = pd.ExcelWriter('Student data.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()
    reader = pd.read_excel(r'Student data.xlsx')
    print(reader)
    
    n3=input("Enter Y to delete another student record or N to return to Main Menu: ")
    
    while (n3 != 'N' and n3 != 'Y'):
            print("Invalid Input")
            n3=input("Enter Y to delete another student record or N to return to Main Menu: ")
            
    if n3 =='N':
        return display_menu()
    
    elif n3 =='Y':
        return delete_student()

with open('password.txt','r') as f:
    lines=f.read()
    n=input("Enter password: ")
    
count = 0

while n != lines:
        count = count + 1
        print("incorrect password \n")
        n=input("Enter password again: ")
        if count == 2 and n != lines:
            print("Too many incorrect attempts")
            break
if n==lines:
        display_menu()
        
        

        
        
        
        
        
        

               
       
       

