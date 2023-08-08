import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
clothing = budget.Category("clothing")
food.deposit(1000, "initial deposit")
food.withdraw(50.54)
food.withdraw(50, "restaurant and more food and fish")

clothing.deposit(1000, "Initial deposit")
food.transfer(50, clothing)
clothing.withdraw(55)
clothing.withdraw(23.23)

print(food)
print(create_spend_chart([food, clothing]))
"""food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))"""