import random
golden_number =random.randint(0,20)

s = 0
n = 5
print("guess the number game......")
print("ok... let's start the game")
while s <= n:
     num = eval(input("input a number in 0 to 20 :-"))
     if num == golden_number:
         print("Congratz....you won the 100mb data....")
         
         input("Enter your number")
         input("☺☺☻☻")
     elif num < golden_number:
         print("try again... your number is less than to the golden number")
         print(n-s,"chances left")
         s = s + 1
     elif num > golden_number:
         print("try again... your number is higher than to the golden number")
         print(n-s,"chances left")
         s = s + 1
     else:
         print("filed")
input("Hhm.........")
input("Press[Enter]")



