class FindPercent: 
  def percentage():
    s1 = int(input("Subject1= "))
    s2 = int(input("Subject2= "))
    s3 = int(input("Subject3= "))
    s4 = int(input("Subject4= "))
    s5 = int(input("Subject5= "))

    total = s1 + s2 + s3 + s4 + s5
    percent = (total / 500) * 100
    print("Total : ", total)
    print("Percentage : ", percent)
    
