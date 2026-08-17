
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))  
mark = int(input("Enter your Marks: "))
cast = input("Enter your Cast (OPEN/ST/NT): ")
income = int(input("Enter Your Annual income: "))
if 18 <= age <= 28:
    if mark >= 85:
        if cast == "OPEN" or cast == "ST" or cast == "NT":
            if income <=200000:
                print("You are eligible")
            else:
                print("Not Eligible due to income.")
        else:
            print("Not eligible due to cast.")
    else:
        print("Not eligible due to marks.")
else:
    print("Not eligible due to age.")
