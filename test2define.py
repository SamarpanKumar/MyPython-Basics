print("""Marilyn works for Integrated Systems, Inc., a software company that has a reputation for providing excellent fringe benefits. One of their benefits is a quarterly bonus that is paid to all employees. Another benefit is a retirement plan for each employee. The company contributes 5 percent of each employee’s gross pay and bonuses to their retirement plans. Marilyn wants to write a program that will calculate the company’s contribution to an employee’s retirement account for a year. She wants the program to show the amount of contribution for the employee’s gross pay and for the bonuses separately. Here is an algorithm for the program:
1. Get the employee’s annual gross pay.
2. Get the amount of bonuses paid to the employee.
3. Calculate and display the contribution for the gross pay.
4. Calculate and display the contribution for the bonuses.""")

def calculate_retirement_contribution(gross_pay, bonuses):
    # Calculate contribution for the gross pay (5% of annual gross pay)
    gross_pay_contribution = 0.05 * gross_pay

    # Calculate contribution for the bonuses (5% of the total bonuses received)
    bonus_contribution = 0.05 * bonuses

    print( gross_pay_contribution, bonus_contribution)

# Input the employee's annual gross pay and bonuses
annual_gross_pay = float(input("Enter the employee's annual gross pay: "))
bonuses_amount = float(input("Enter the amount of bonuses paid to the employee: "))

# Calculate the retirement contributions
gross_pay_contribution, bonus_contribution = calculate_retirement_contribution(annual_gross_pay, bonuses_amount)

# Display the results
print(f"Contribution for gross pay: ${gross_pay_contribution:.2f}")
print(f"Contribution for bonuses: ${bonus_contribution:.2f}")
