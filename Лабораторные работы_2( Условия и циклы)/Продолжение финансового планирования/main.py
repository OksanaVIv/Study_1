salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
salary_total = salary
spend_total = spend
for i in range(months-1):
    spend *= 1 + increase
    salary_total += salary
    spend_total += spend
money_capital = int(spend_total - salary_total)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

