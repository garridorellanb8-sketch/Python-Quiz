print("Hello and welcome to my Quiz about Python!")
score=0 
print("What prints a question and waits for your answer?")
answer=input("a:Input or b:Print ? ").lower()
if answer=="a":
    print("Correct!")
    score+=1
else:print("Incorrect!")
print()
print("Which one is in python correct?")
answer=input("a:Best friend or b:Best_friend? ").lower()
if answer=="b":
    print("Correct!")
    score+=1
else: print("Incorrect!")
print()
print("which commando do I have to use when I want to print a whole number?")
answer=input("a:str or b:float or c:int? ").lower()
if answer=="a":
    print("Incorrect!")
elif answer=="c":
    print("Correct!")
    score+=1
else:print("Incorrect!")
print()
print("LAST QUESTION!")
print()
print("What makes .lower()?")
answer=input("a:writes the user-s answer in lowercase or b:writes the user-s answer in uppercase? ").lower()
if answer== "a":
    print("Correct!")
    score+=1
else:print("Incorrect!")
print()
print("Thank you for playing my python Quiz!")
print()
print(f"You scored {score} points!")
if score==4:
    print("Hey you are a very good python begginer!")
elif score==3 or score==2:
     print("Hey not bad i think you could be good in python!")
else: print("Hey that was probably your first time hearing about Python. If you are interested," \
" I recommend trying Coddy,Codedex, or mimo.These sites let you learn and practice Pyton as well as other programming languages.")
print()
print("I hope you liked my Quiz")
