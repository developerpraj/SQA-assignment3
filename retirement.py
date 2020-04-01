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
