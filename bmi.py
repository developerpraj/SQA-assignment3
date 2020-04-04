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