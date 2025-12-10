from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

model = LpProblem("production_optimization", LpMaximize)

lemonade = LpVariable("lemonade", lowBound=0, cat="Integer")
juice = LpVariable("juice", lowBound=0, cat="Integer")

model += lemonade + juice

model += 2 * lemonade + 1 * juice <= 100
model += 1 * lemonade <= 50
model += 1 * lemonade <= 30
model += 2 * juice <= 40

model.solve()

print("Лимонад:", value(lemonade))
print("Фруктовий сік:", value(juice))
print("Максимум продукції:", value(lemonade + juice))