
import random
class dice:
    
    def __init__(self ):
        
        self.min = 1
        self.max = 6

        self.roll_again = "yes"


    def roll(self):
        while self.roll_again == "yes" or self.roll_again == "y":
            print ("Rolling the dices...")
            print ("The values are....")
            print (random.randint(self.min, self.max))
            print (random.randint(self.min, self.max))

            self.roll_again = input("Roll the dices again?")
        self.roll_again = "y"