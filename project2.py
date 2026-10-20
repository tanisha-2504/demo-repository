print("Welcome to the pattern generator and number analyzer!") 
while(True):
    print(''' Select an option:  
              1.Generate a pattern
              2.Analyze a range of Numbers
              3.Exit''')
    userinput = int(input("Enter your choice: "))
    if (userinput==1):
        numofrows = int(input("enter the number of rows for the patterns: "))
        for i in range (numofrows):
            for j in range(i+1):
                print("*", end='')
            print() 
    elif (userinput==2):
        startnum = int(input("enter the start of the range: "))
        endnum = int(input("enter the end of the range: "))
        sum=0
        for i in range(startnum,endnum+1):
            sum=sum+i
            if i%2==0 :
                print(f"number {i} is Even")
            else:
                print(f"number {i} is odd")        
        print(f"sum of all numbers from {startnum} to {endnum} is : {sum} ")        
        print()  
    elif (userinput==3):
        print("Exiting the program. Goodbye!")    
        break
    else:
        print("invalid choice")    
print("out of loop")





    