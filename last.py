# Input values
initial_investment = 1000000
units_allotted_on_purchase = 271.57
nav_on_redemption_date = 3737.30240

# Calculate the value of units on the redemption date
value_on_redemption_date = units_allotted_on_purchase * nav_on_redemption_date

# Calculate net profit
net_profit = value_on_redemption_date - initial_investment

# Print the results
print(f"Value of {units_allotted_on_purchase} units on 18-10-2023: ${value_on_redemption_date:.2f}")
print(f"Net Profit: ${net_profit:.2f}")
