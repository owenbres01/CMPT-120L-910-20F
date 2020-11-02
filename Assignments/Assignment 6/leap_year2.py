def leap_year(year):
    leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      leap = True
  else:
      leap = False

  return leap

if __name__ == "__main__":
    years = [2004, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)