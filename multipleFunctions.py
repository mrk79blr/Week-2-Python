class multipleFunctions: 
  def triangle():
    print("To calculate Perimeter and Area of a triangle")
    height = float(input("Height:"))
    breadth = float(input("Breadth:"))
    area = (height * breadth) / 2
    print("Area formula: (Height*Breadth)/2")
    print("Area of Triangle: ", area)

    height1 = float(input("Height1:"))
    height2 = float(input("Height2:"))
    breadth = float(input("Breadth:"))
    perimeter = height1 + height2 + breadth
    print("Perimeter formula: Height1+Height2+Breadth")
    print("Perimeter of Triangle: ", perimeter)
  
  def Subfields():
        list = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Printing a List")
        print("Sub-fields in AI are:")
        for field in list:
            print(field)
  def OddEven():
    print("To find odd/Even")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is Even number")
    else:
        print(num, "is Odd number")

  def percentage():
    print("To calculate the Percentage of 5 subjects")
    s1 = int(input("Subject1= "))
    s2 = int(input("Subject2= "))
    s3 = int(input("Subject3= "))
    s4 = int(input("Subject4= "))
    s5 = int(input("Subject5= "))

    total = s1 + s2 + s3 + s4 + s5
    percent = (total / 500) * 100
    print("Total : ", total)
    print("Percentage : ", percent)
    
  def Eligible():
    print("Enter male/female and age to know the whether you are eligibile for the marriage")
    gender = input("Your Gender: ")
    age = int(input("Your Age: "))

    if gender.lower() == "male" and age >= 21:
        print("ELIGIBLE")
    elif gender.lower() == "female" and age >= 18:
        print("ELIGIBLE")
    else:
        print("NOT ELIGIBLE")
