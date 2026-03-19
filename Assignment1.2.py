name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - 500   # LIC deduction

print("\n--- Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction: 500")
print("Net Salary:", net_salary)Priya
