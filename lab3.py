customer_name = input("Enter your name: ")
monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter the loan amount you are requesting: "))

# Comparison operator to check salary eligibility
if monthly_salary >= 3000:
    # Check loan amount using comparison and logical operators
    if loan_amount <= 10 * monthly_salary:
        print(f"\nCongratulations, {customer_name}! Your loan request of ${loan_amount:.2f} is approved.")
    else:
        print(f"\nSorry, {customer_name}. The requested loan amount of ${loan_amount:.2f} exceeds the limit (10 times your salary).")
else:
    print(f"\nSorry, {customer_name}. You are not eligible for the loan as your monthly salary is below $3000.")

# Output: Display the user's details
print(f"Monthly Salary: Php{monthly_salary:.2f}")
print(f"Loan Amount Requested: Php{loan_amount:.2f}")
