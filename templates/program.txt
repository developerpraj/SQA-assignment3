#  Name: Prajjwol Timilsina
# Net-ID: pt439
# Description: An application That calculates your BMI and  Retirement Plan;


#defining BMI Function




def bmi(mass,height):
   
    massInKg = mass*0.45
    heightInMeters = height*0.025
    heightFactor = heightInMeters**2
    bodyMassIndex = massInKg/heightFactor
    if bodyMassIndex <= 18.5:
        print("\n\tBody Mass Index(BMI):",
            bodyMassIndex, "\n\tCategory : Underweight")

    elif (18.5 <= bodyMassIndex <= 24.9):
        print("\n\tBody Mass Index(BMI):",
            bodyMassIndex, "\n\tCategory : Normal weight")

    elif (25 <= bodyMassIndex <= 29.9):
        print("\n\tBody Mass Index(BMI):",
            bodyMassIndex, "\n\tCategory : Overweight")

    else:
        print("\n\tBody Mass Index(BMI):", bodyMassIndex, "\n\tCategory : Obese")
    return bodyMassIndex
  


#Refitirement Function
def Retiremnet(age,Annual_Salary,goal,percent):
    Employer_Assist= 0.35*((percent/100)*Annual_Salary)
    Total_savings_per_year=Employer_Assist+((percent/100)*Annual_Salary)
    timerequired=goal/Total_savings_per_year
    retirementAge=timerequired+age
    if retirementAge>100:
        print("Your Retirement Goal Can't be met unless you Increase Your Saving. \n Your age will be above 100 i,e",format(retirementAge, '1.0f'),"years")
    else:
        print("Your Savings will be met when you will be",format(retirementAge, '1.0f')," Years." )
    return retirementAge

 #defining Header
def header():
    print("For BMI----------------------Press '1'")
    print("For Retirement Plan----------Press '2'")
    print("To Quit----------------------Press '3'")


#Defing Closing Function
def close():
    exit = input("Please enter 'q' to conform you are quiting ").lower()
    if 'q' in exit:
        print("Goodbye")
        quit()
    else:
        print("Returning to Main Menu")
        main()

#Definig Back To menu
def back_to_menu():
    back = str(input("\n\n\tplease press m to return to main menu:   "))
    if back == "m" or back == "M":
        main()
    if back != "m":
        try:
            print("Please enter lowercase m: ")
        except ValueError as err:
            print(err)

        finally:
            print("Moving you to main menu")
            main()

#____________________________________________________________________-#prorgam Starts from here._____________________________________________
def main():
    mass=0
    height=0
    age=0
    Annual_Salary=0
    goal=0
    percent=0
    choice=0
    header()
    try:
      choice = int(input("\n\t Please Make a Selection: "))
           
    except (TypeError,ValueError,AssertionError) as err:
        choice = int(input("\n\t Please Make a Selection: "))
           
    finally:
        if choice == 1 or choice == 2 or choice== 3:

            if choice == 1:
                try:
                    mass = float(input("Please Enter the mass of your body in Pounds:"))
                    assert(mass>=1),"\n Error: Mass should be Positive."
                except (TypeError,ValueError,AssertionError) as err:
                    print("\n\tPlease Enter A Positive Number for the Input To Be valid.")
                    mass = float(input("Please Enter the mass of your body in Pounds:"))

                finally:
                    if mass<1 or type(mass) is not float:
                        back_to_menu()
                    else:
                        pass


                try:
                    height = float(input("Please Enter the Height of your body in Inches:"))
                    assert(height>=1),"\nHeight should be a Positive Number."
                except (TypeError,ValueError,AssertionError) as err:
                   print("\n\tPlease Enter A Positive Number for the Input To Be valid.")
                   height = float(input("Please Enter the Height of your body in Inches:"))
                    
                finally:
                     if height<1 or type(height) is not float:
                        back_to_menu()
                     else:
                        pass

                bmi(mass,height)
                back_to_menu()

            elif choice == 2:
                try:
                    age = int(input("Please Enter your Current Age: "))
                    assert(1<=age<=100),"Age should be Positive"
                except (TypeError,ValueError,AssertionError) as err:
                    print("Please enter a Positive number for the input to be valid (age cant be above 100)")
                    age = int(input("Please Enter your Current Age: "))  
                finally:
                     if age<1 or age>100 or type(age) is not int:
                        back_to_menu()
                     else:
                        pass
                    
                try:
                    Annual_Salary= int(input("Please Enter your Annual Salary in $$:$ "))
                    assert(Annual_Salary>=1),"Annual Salary should be Positive"
                except (TypeError,ValueError,AssertionError) as err:
                    print("Please enter a Positive Number for the Input To Be valid.")
                    Annual_Salary= int(input("Please Enter your Annual Salary in $$:$ "))
                finally:
                     if Annual_Salary<1 or type(Annual_Salary) is not int:
                        back_to_menu()
                     else:
                        pass
                    
                try:
                    goal = float(input("Please Enter your Retiremnet Goal: "))
                    assert(goal>=1),"Goal should be not be Negative"

                except (TypeError,ValueError,AssertionError) as err:
                    print("Please enter a Positive Number for the Input To Be valid.")
                    goal = float(input("Please Enter your Retiremnet Goal: "))
                finally:
                     if goal<0 or type(goal) is not float:
                        back_to_menu()
                     else:
                        pass
                    

                try:
                    percent= float(input("What percent are you saving each year: "))
                    assert(1<=percent<=100),"Percent should not be Negative and greater than 100% "
                except (TypeError,ValueError,AssertionError,ZeroDivisionError) as err:
                    print("Percent should not be Negative and greater than 100%\nYou should save atleast 1% to calculate your Retirement plan")
                    percent= float(input("What percent are you saving each year: "))
                finally:
                     if percent<=0 or percent >100 or type(percent) is not float:
                        back_to_menu()
                     else:
                        Retiremnet(age,Annual_Salary,goal,percent)
                        back_to_menu()

            elif choice == 3:
                close()
        
        else:
            print("INVALID INPUT")
            print("Redirecting to Main Menu")
            main()
        
     

#calling the Main Function
main()

