import hashlib
from datetime import datetime
import calendar
class account:
    def __init__(self, balance):
        self.balance = balance
        self.goal = []
        self.monthly_limit = None
        self.spent_this_month = 0
        self.budget_month = datetime.now().month
        self.daily_spending = {}
    def set_monthly_limit(self, limit):
        if limit > 0:
            self.monthly_limit = limit
            self.spent_this_month = 0
            self.budget_month = datetime.now().month
            print("Monthly limit set to " + str(limit))
        else:
            print("Invalid amount")
    def budget_month_reset(self):
        if datetime.now().month != self.budget_month:
            self.spent_this_month = 0
            self.budget_month = datetime.now().month
            print("New month limit reset.")
    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid amount")
            return
        if amt > self.balance:
            print("Insufficiant balance")
            return
        if self.monthly_limit is not None:
            self.budget_month_reset()
            if amt + self.spent_this_month > self.monthly_limit : 
                print("Amount is greater than the monthly limit")
                return
            if amt + self.spent_this_month > self.monthly_limit * 0.8:
                print("Warning: this transaction will use up more than 80% of your budget")
        purpose = input("Enter the reason of this transaction: ")
        self.balance -= amt
        today = str(datetime.now().date())
        self.daily_spending[today] = self.daily_spending.get(today, 0) + amt
        self.spent_this_month += amt
        print("Withdrawl successful. Reason for withdrawl: " + purpose)
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
                if amt < i[1] and amt > 0 and amt <= self.balance:
                    i[1] -= amt
                    self.balance -= amt
                elif amt == i[1]:
                    print("Goal complete " + i[0])
                    self.balance -= amt
                    self.goal.pop(self.goal.index(i))
                elif amt > self.balance:
                    print("More than balance amount")
                else:
                    print("More than goal amount")
    def calendar(self):
        date_and_time = str(datetime.now().date())
        print("Total balance left on "+ date_and_time + " is " + str(self.balance))
        for date, spent in self.daily_spending.items():
            print("Spent on " + date + ": " + str(spent))
users = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def register(username,password,initial_bal):
    if username in users:
        print("User is already registered")
        return
    users[username] = {"Password": hash_password(password),"Balance": account(initial_bal)}   
    print("User created successfully")
def login(username, password):
    if username not in users:
        print("Username not found")
        return None
    if users[username]["Password"] != hash_password(password):
        print("Incorrect password")
        return None
    print("Welcome, " + username + "!")
    return users[username]["Balance"]