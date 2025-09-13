# this is basic finance calculator project based on one's total income and expenses in a month
monthly_income = float(input("Enter monthly income"))
monthly_expenses = float(input("Enter total monthly expenses"))
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings  are, {monthly_savings}")

#The projected savings in a year based on an interest rate of five percent 

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year with interest  are, {projected_savings}")