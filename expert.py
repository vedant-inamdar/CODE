import math
print()
print("Answer the questions 1 or 0")
print()
s1=bool(int(input("Sweating")))
s2=bool(int(input("Shivering?")))
s3=bool(int(input("Dehydration")))
s4 = bool(int(input("Runny Nose? ")))
s5 = bool(int(input("Sore Throat? ")))
s6 = bool(int(input("Weakness? ")))
s7 = bool(int(input("Headache? ")))
s8 = bool(int(input("Vomitting? ")))
s9 = bool(int(input("Nausea? ")))
s10 = bool(int(input("Pale Stool? ")))
s11 = bool(int(input("Itching? ")))
s12 = bool(int(input("Dark Urine? ")))
s13 = bool(int(input("Yellowing of Stool? ")))
s14 = bool(int(input("Pain? ")))

if(s1==True and s3==True and s6==True and s12==True):
    print("Detected: \nCough \nRemedy: Benedryl, \nDrink Hot Water")

elif(s4==True and s5==True and s6==True and s8==True):
    print("Detected: Cough \n Remedy: Benedryl, Drink Hot Water")

elif (s8 == True and s10 == True and s12== True and s13 == True):
    print ("Detected: Stomach Infection \n Remedy: Benedryl, Drink Hot Water")

elif (s2 == True and s10 == True and s6== True and s8 == True and s13 == True and s14 ==True):
    print ("Detected: Jaundice \n Remedy: No home remedy, go to Hospital")
else:
    print ("No Disease Detected. Consult a Doctor!")
print()