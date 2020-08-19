class player:
    print("\n")
    def __init__(self, name: str, money: int ):
        self.name = name
        self.money = money
   
     

    def loss(self, amount: int):
        self.money-=amount
        #print("\n")
        return print(self.name,self.money)

    def won(self, amount:int):
        self.money+= amount
        #print("\n")
        return print(self.name, self.money)


