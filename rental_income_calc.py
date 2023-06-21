class rental_income_calculator():

    def __init__(self, income, expenses, cashFlow, investment, goalReturn):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cashFlow
        self.investment = investment
        self.goal = goalReturn


    def monthlyIncome(self):
        print("\nThis shows your monthly income.")
        self.income += float(input("What is your total monthly income?: "))
        print(f"Your total income is ${round(self.income, 2)}")


    def monthlyExpenses(self):
        print("\nThis shows your monthly expenses.")
        self.expenses += float(input("Mortgage/rent: "))
        self.expenses += float(input("water: "))
        self.expenses += float(input("Electric/gas: "))
        self.expenses += float(input("Car payment: "))
        self.expenses += float(input("Car insurance: "))
        self.expenses += float(input("Housing amenities: "))
        self.expenses += float(input("Total of other expenses: "))
        print(f"Your total monthly expenses is ${round(self.expenses, 2)}")


    def totalCashFlow(self):
        self.cashFlow = (self.income - self.expenses) * 12
        print(f"This is your annual cashflow ${round(self.cashFlow, 2)}")


    def totalInvestment(self):
        self.investment += float(input("Down payment: "))
        self.investment += float(input("Price of property: "))
        print(f"This is your total investment ${round(self.investment, 2)}")


    def goal_return(self):
        self.goalReturn = (self.cashFlow / self.investment) * 100
        print(
            f"This is your estimate cash return goal: {round(self.goal, 2)}%")


RentalIncome = rental_income_calculator(0, 0, 0, 0, 0)




def run():
    while True:
        response = input(
            "Hello! Welcome to Rental Income Calculator!\n Please select the following option.\nType one of the following option: use / quit:\n").lower()

        if response == "use":
            RentalIncome.monthlyIncome()
            RentalIncome.monthlyExpenses()
            RentalIncome.totalCashFlow()
            RentalIncome.totalInvestment()
            RentalIncome.goal_return()
        elif response == "quit":
            print("Thank you for using our Rental Income Calculator! Goodbye!")
            break
        else:
            print("Please enter a different option!")


run()