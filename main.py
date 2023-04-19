# Filename: main.py

"""
This program creates a user interface to input and output values for the AppInvest app.
"""

"""Import each of the three functions into main.py"""
import calculate_gains as cg
import calculate_gains_over_time as ct
import functions_optional as fo

"""Request user input"""
amount_inv = float(input("Enter amount to invest (USD): $"))
while amount_inv < 1000:
    amount_inv = float(input("Entry not valid. Enter an amount of at least $1000 (USD): $"))
period = int(float(input("Enter period to invest (in months): ")))
print("")  # adds visual space between blocks of content

"""Call functions to calculate"""
# Gain for one month
gains_first_month, amount_inv_first_month, gain_margin = cg.calculate_gains(amount_inv)
formatted_value, currency = fo.format_currency(gains_first_month)  # format to USD

# Gain over period of months (default is 12 months)
total_amount_inv, total_gains, period, gain_margin = ct.calculate_gains_over_time(amount_inv, period)
formatted_value, currency = fo.format_currency(total_gains)  # format to USD

"""Print the output formatting to US dollars with 2 decimals places"""
# Amount to invest (from user input above)
formatted_value, currency = fo.format_currency(amount_inv)  # format to USD
print("Amount invested:", formatted_value, currency)

# Total Amount after 1 month (from calculate_gain function)
formatted_value, currency = fo.format_currency(amount_inv_first_month)  # format to USD
print("Total amount after 1 month:", formatted_value, currency)

# Total Gain after 1 month (from calculate_gain function)
formatted_value, currency = fo.format_currency(gains_first_month)  # format to USD
print("Total gain after 1 month:", formatted_value, currency)

# Gain margin based on amount invested (from calculate_gain function)
print("Gain margin based on amount invested:", round((gain_margin * 100), 2), "%")  # multiplied gain_margin by 100 to convert from decimal to percent

# Investment period (from user input above)
print("Investment period:", period, "months")

# Total amount invested after period (from calculate_gain_over_time function)
formatted_value, currency = fo.format_currency(total_amount_inv)  # format to USD
print("Total amount invested after investment period:", formatted_value, currency)

"""Test Cases"""
# Test Case 1: Invalid entry
# amount_inv = 500
# EXPECTED RESULTS:
# Entry not valid. Enter an amount of at least $1000 (USD):

# Test Case 2: Minimum amount invested
# amount_inv = 1000
# period = 12
# EXPECTED RESULTS:
# Amount invested: $1000.00 USD
# Total amount after 1 month: $1001.00 USD
# Total gain after 1 month: $1.00 USD
# Gain margin based on amount invested: 0.1 %
# Investment period: 12 months
# Total amount invested after investment period: $1012.07 USD

# Test Case 3: Multiplier applied
# amount_inv = 999999
# period = 12
# EXPECTED RESULTS:
# Amount invested: $999999.00 USD
# Total amount after 1 month: $1000999.00 USD
# Total gain after 1 month: $1000.00 USD
# Gain margin based on amount invested: 1.1 %
# Investment period: 12 months
# Total amount invested after investment period: $1129006.27 USD

# Test Case 4: Large amount invested
# amount_inv = 11000000
# period = 12
# EXPECTED RESULTS:
# Amount invested: $11000000.00 USD
# Total amount after 1 month: $12221000.00 USD
# Total gain after 1 month: $1221000.00 USD
# Gain margin based on amount invested: 100 %
# Investment period: 12 months
# Total amount invested after investment period: $482414496.96 USD

# Test Case 5: Non-default period (default period is 12 months)
# amount_inv = 3000000
# period = 18
# EXPECTED RESULTS:
# Amount invested: $3000000.00 USD
# Total amount after 1 month: $3093000.00 USD
# Total gain after 1 month: $93000.00 USD
# Gain margin based on amount invested: 5.1 %
# Investment period: 18 months
# Total amount invested after investment period: $5722920.55 USD
