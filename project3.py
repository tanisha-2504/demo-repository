student=[]
print("Welcome to the student data organizer!")

while(True):
    print('''Select an option
    1.Add Student
    2.Display All Students
    3.Update Student Information
    4.Delete Student
    5.Display Subjects Offered
    6.Exit''')

    userinput=int(input("Enter your choice: "))

    if (userinput==1):
        print("Enter student details:")
        studentid=int(input("Student ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        grade=input("Grade: ")
        dob=input("Date of Birth (YYYY-MM-DD): ")
        subjects=input("Subjects (comma-separated): ")
        uniqueinfotupel=(studentid,dob)

        studentdic={
            "studentid":studentid,
            "name":name,
            "age":age,
            "grade":grade,
            "dob":dob,
            "subjects":set(subjects.split(","))
        }
        student.append(studentdic)
        print("Student added successfully!")

    elif(userinput==2):
        for i in student:
            print(f"Student ID: {i['studentid']} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']} | DOB: {i['dob']} | Subjects: {i['subjects']}")

    elif(userinput==3):
        userinputstdID=int(input("Enter Student ID to Update: "))
        for i in student:
            if(i['studentid']==userinputstdID):
                print('''
                         1. Update Name
                         2. Update Age
                         3. Update Grade
                         4. Update Subjects
                         ''')
                updatechoice=input("what do you want to update? : ")
                if updatechoice == "1":
                    i['name'] = input("Enter new name: ")
                elif updatechoice == "2":
                    i['age'] = int(input("Enter new age: "))
                elif updatechoice == "3":
                    i['grade'] = input("Enter new grade: ")
                elif updatechoice == "4":
                    subjects = input(" Enter new Subjects (comma-separated): ") 
                    i['subjects'] = set(subjects.split(","))
                else:
                    print("Invalid choice")
                    break
                print("student information updated successfully!")
                break
            else:
                print("student ID not found!")

    elif(userinput==4):
        stdId = int(input("Enter Student ID to delete: "))
        for i in student:
            if i["studentid"] == stdId:
                student.remove(i)
                print("Student deleted!")
                break
        else:
                print("student not found!")

    elif(userinput==5):
        for i in student:
            print(f"student id {i['studentid']} | Subjects offered: {i['subjects']}")

    elif(userinput==6):
        print(" Thank you for using Student Data Oraganizer!")
        break
    else:
        print("Invalid choice, please try again.")







        

    