class account:
    def __init__(self, balance):
        self.balance = balance
        self.goal = []
    def withdraw(self, amt):
        if amt <= self.balance and amt > 0:
            self.balance = self.balance - amt
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            print("Deposit successful")
        else:
            print("Invalid amount")
    def create_goal(self,goal_name,goal_amt):
        self.goal.append([goal_name,goal_amt])
    def add_to_goal(self, goal_name, amt):
        for i in self.goal:
            if i[0] == goal_name:
                if amt < self.goal_amt and amt > 0:
                    self.goal_amt -= amt
                elif amt == self.goal_amt:
                    print("Goal complete " + self.goal_name)
                    self.goal.pop(i)
                else:
                    print("More than goal amount")
                