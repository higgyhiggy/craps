from player import player
from dice import dice



name = input("p1 name: ")
money= int(input("p1 money:"))

print("\n")

name2=input("p2 name: ")
money2=int(input("p2 money: "))

p1= player(name,money)
p2=player(name2,money2)
dices = dice()


while(True):
    print("\n")

    amount=int(input("amount to bet: "))
    dices.roll()
    print("\n")
    player=int(input("which player lost? "))
    if player ==1:
        p1.loss(amount)
        p2.won(amount)
    else:
        p2.loss(amount)
        p1.won(amount)
    print("\n")
