# Grade calculator
math = float(input("Enter Maths marks: "))
if math <= 100:
    eng = float(input("Enter English marks: "))
    if eng <= 100:
        phy = float(input("Enter Physics marks: "))
        if phy <= 100:
            # check if marks are greater than 40
            if math < 40 and phy < 40 and eng < 40:
                print("Failed")
            elif math < 40 and phy < 40:
                print("You failed both in Physics and in Maths")
            elif math < 40 and eng < 40:
                print("You failed both in English and in Maths")
            elif phy < 40 and eng < 40:
                print("You failed both in English and in Pysics")
            elif math < 40:
                print("You failed in Maths")
            elif eng < 40:
                print("You failed in English")
            elif phy < 40:
                print("You failed in Physics") 
            else:
                obtainedMarks = math + eng + phy
                percentage = (obtainedMarks / 300)  * 100
                
                marks = round(obtainedMarks)
                percent = round(percentage)
                
                if percentage >= 80:
                    print("Obtained Marks -> " + str(marks) + "/100 : " + "Percentage -> " + str(percent) + "% : " + "Grade -> A+")
                elif percentage >= 70:
                    print("Obtained Marks -> " + str(marks) + "/100 : " + "Percentage -> " + str(percent) + "% : " + "Grade -> A")
                elif percentage >= 60:
                    print("Obtained Marks -> " + str(marks) + "/100 : " + "Percentage -> " + str(percent) + "% : " + "Grade -> B")
                elif percentage >= 50:
                    print("Obtained Marks -> " + str(marks) + "/100 : " + "Percentage -> " + str(percent) + "% : " + "Grade -> C")
                elif percentage >= 40:
                    print("Obtained Marks -> " + str(marks) + "/100 : " + "Percentage -> " + str(percent) + "% : " + "Grade -> D")
        else:
             print("Marks must be out of hundred!")             
    else:
        print("Marks must be out of hundred!")
else:
    print("Marks must be out of hundred!")




