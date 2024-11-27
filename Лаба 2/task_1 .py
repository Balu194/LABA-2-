money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = 0
while money_capital + salary * i > spend * i:
        i = i + 1
        spend += spend * increase

print(i)
