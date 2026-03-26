name = input("Enter Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

salary = basic + da + hra + ta - lic

print("\n--- Employee Details ---")
print("Name:", name)
print("ID:", emp_id)
print("Department:", dept)
print("Net Salary:", salary)


# 2
name = input("Vendor Name: ")
year = input("Year of Association: ")
contact = input("Contact Number: ")
email = input("Email ID: ")

total = 0
for i in range(12):
    amt = float(input(f"Enter purchase for month {i+1}: "))
    total += amt

print("\nAnnual Purchase:", total)