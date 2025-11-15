class EligibilityForMarriage: 
  def Eligible():
    gender = input("Your Gender: ")
    age = int(input("Your Age: "))

    if gender.lower() == "male" and age >= 21:
        print("ELIGIBLE")
    elif gender.lower() == "female" and age >= 18:
        print("ELIGIBLE")
    else:
        print("NOT ELIGIBLE")


    
