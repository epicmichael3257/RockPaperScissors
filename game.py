# Write your code here
import random as r

name = input("Enter your name:")   #ask for name
print("Hello,",name)
newName = False
d = {}
with open("rating.txt",'rt') as f:   #create dictionary from list values
    for line in f:
        a = line.split()
        key,values = a[0],int(a[1])
        d[key] = values
f.close()
if name not in d: #initalize them if they don't already exist --add them to file at the end
    d[name] = 0
    newName = True





player = ""


while player != "!exit": #yes the code could be condensed but do i care? no. should i? probably lol
    player = input()
    player = player.lower()
    if player == "scissors" or player == "paper" or player == "rock":
        computer_responses = ["scissors", "paper", "rock"]
        computer_response = r.randint(0, 3)
        if player == "scissors":
            if computer_response == 0:
                print("There is a draw (scissors)")
                d[name] += 50
            elif computer_response == 1:
                print("Well done. The computer chose paper and failed")
                d[name] += 100

            else: print("Sorry, but the computer chose rock")
        elif player == "paper":
            if computer_response == 0:print("Sorry, but the computer chose scissors")
            elif computer_response == 1:
                print("There is a draw (paper)")
                d[name] += 50
            else:
                print("Well done. The computer chose rock and failed")
                d[name] += 100
        elif player == "rock":
            if computer_response == 0:
                print("Well done. The computer chose scissors and failed")
                d[name] += 100
            elif computer_response == 1:print("Sorry, but the computer chose paper")
            else:
                print("There is a draw (rock)")
                d[name] += 50
    elif player != "!exit" and player != "!rating":
           print("Invalid input")
    elif player == "!rating":
        print("Your rating",d[name])

if newName:
        with open('rating.txt','a') as f:
            f.write(name+" "+str(d[name])+"\n")
            f.close()
else:   # write overwrite rating file at just that line OR rewrite it and keep everything except that line
        with open('rating.txt','wt') as new:
            for key in d:
                new.write(key+" "+str(d[key])+"\n")
print("Bye!")


