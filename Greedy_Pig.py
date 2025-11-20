#Import required modules
import random
import json

#Set variables
DiceSides = int(input("How many sides would you like to have on your dice?"))
DeadNumber = int(input("Please enter number."))
RoundNumber = 1
Score = 0
try:
    with open("highscore.json", "r"):
        data = json.load(f) 
        HighScore = data["Highscore"]
except FileNotFoundError:
    HighScore = 0

#Defines Game Over function
def GAME_OVER():
    global HighScore
    print ("GAME OVER Score:", Score)
    if Score > HighScore:
        print ("NEW HIGH SCORE!!!!")
        print ("New High Score:", Score)
        print ("Old High Score:", HighScore)
        HighScore = Score
        with open("highscore.json", "w") as f:
            json.dump({"HighScore": HighScore}, f)
    data = {"HighScore": HighScore}
    exit()

#Starts Game
while True:
    DiceNumber = random.randint(1, DiceSides)
    if DiceNumber == DeadNumber :
        GAME_OVER()
    print ("Round", RoundNumber, ":")
    print(   "Dice:", DiceNumber)    
    Score = Score + DiceNumber
    if input("Sit or Stay? 1. Sit 2. Stay") == 2 :
        GAME_OVER