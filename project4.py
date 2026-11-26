print("Welcome to the data analyzer and transformer program")
data=[]

while True:
    print('''Main Menu:
    1. Input Data
    2. Display Data Summary
    3. Calculate Factprial
    4. Filter Data by Threshold
    5. Sort Data
    6. Display Dataset Statistics
    7. Exit Program''')

    choice = input("Please enter your choice: ")

    if choice == "1":
        values = input("Enter numbers separated by spaces: ")
        data = list(map(int,values.split()))
        print("Data stored successfully!")

    elif choice == "2":
        print("Total elements:",len(data))
        print("minimum:",min(data))
        print("maximum:",max(data))    
        print("sum:",sum(data))
        print("average:",sum(data)/len(data))

    elif choice == "3":
        def factorial(n):
            if n<=1:
                return 1
            return n * factorial(n-1)

        num = int(input("enter a number to calculate its factorial: "))
        print("factorial of",num,"is:", factorial(num))
     
    elif choice == "4":
        threshold = int(input("Enter a threshold value to filter out data above this value: "))
        result = list(filter(lambda x: x>=threshold,data))
        print("Filtered data:",result)

    elif choice == "5":
        print("Choose sorting option:")
        print ("1.Ascending")
        print("2.Descending")

        option = input("enter your choice: ")
        if option == "1":
            data.sort()
            print("Sorted data in Ascending Order:",data)

        elif option == "2":
            data.sort(reverse=True)
            print("Sorted data in Descending Order:",data)

        else:
            print("Invalid choice!")

    elif choice == "6":
        print("Dataset Statistics:")
        print("minimum:",min(data))
        print("maximum:",max(data))    
        print("sum:",sum(data))
        print("average:",sum(data)/len(data))

    elif choice == "7":
        print("Thank you for using the Data Analyzer and Transformer program. Goodbye!")
        break

    else:
        print("Invalid Choice!")    
