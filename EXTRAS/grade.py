#VERSION 1.0

score = int(input("Enter your total score : "))
if score >=90 and score <= 100:
    print("Your grade is A ")
elif score >=80 and score <90:
    print("your grade is B ")
else:
    print("you are average ok Nigga !") 

#VERSION 2.0 (MORE OPTIMIZED)

score = int(input("Enter your score : "))
if 90<= score <=100:
    print("Congratualtions ! You got A+")
elif 80<= score <90:
    print("Congratulations! You got an A !")

#VERSION 3.0 (MORE AND MORE OPTIMIZED LOGICALLY)

score = int(input("Enter your percentage : "))
if score >=90:
    print("You got an A+")
elif score>=80:
    print("You got an A !")
elif score>=70:
    print("You got B+ ")
