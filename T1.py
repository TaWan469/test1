class wallet():
    def __init__(self, money):
        self.money = money

    def give(self, x):
        self.money + x

    def spend(self, x):
        self.money - x

    def __str__(self):
        return f"\n\n\nYou have All money {self.money} Coin\n\n\n"