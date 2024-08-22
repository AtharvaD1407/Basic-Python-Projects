# About:
#     This is a 2 player cricket game that we used to play in school using our fingers.
#     You just have to select which player will go to bat first.
#     It will display the Batsman Score and how may balls it took it take him down.

# Note - If you want take input you can take input on line number 23 and 24.

import random as r

batOut = False
score = 0
p1Score, p2Score = 0, 0
balls = 1

choice = int(input("Enter who is the batsman: "))
match choice:
    case 1:
        score = p1Score
    case 2:
        score = p2Score

while not batOut:
    p1 = r.randint(1, 6)
    p2 = r.randint(1, 6)
    
    balls += 1
    
    if p1 == p2:
        batOut = True
    
    if score == p1Score:
        score += p1
    else:
        score += p2

print(f"Batsman Scored  = {score} in {balls} balls")    
