def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0): 
        leap = True
        print("is leap year")
    elif (year % 100 == 0) and (year % 400 != 0):
        leap = False
        print("is not leap year")
    elif (year % 400 == 0):
        leap = True
        print("is leap year")
    else:
        leap = False
        print("is not leap year")

        return leap

if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)