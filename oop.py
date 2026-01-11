import random

class GuessGame:
    def __init__(self):
       self.secret = random.randint(1,10)
    
    def play(self):
       print("Welecome to the Guess Game!")
       guess = int(input("Guess a number between 1 and 10: "))

       if guess == self.secret:
            print("CORRECT YOU WIN!!")
       else:
            print(f"YOUR WRONG the wrong number was {self.secret}")

#create an object
game = GuessGame()
game.play()