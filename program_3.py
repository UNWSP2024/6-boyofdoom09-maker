# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
def calculate_sales_tax(total_sales):
    county_rate = 0.025
    state_rate = 0.05
    county_tax = total_sales * county_rate
    state_tax = total_sales * state_rate
    total_tax = county_tax + state_tax
    return county_tax, state_tax, total_tax

try:
    monthly_sales = float(input("Enter the total sales for the month: "))
    county_tax, state_tax, total_tax = calculate_sales_tax(monthly_sales)
    print("\nCounty sales tax: ${:.2f}".format(county_tax))
    print("State sales tax:  ${:.2f}".format(state_tax))
    print("Total sales tax:  ${:.2f}".format(total_tax))
except ValueError:
    print("Invalid input. Please enter a valid number.")
# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
