# Taking input from user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

# Calculate current
current = voltage / resistance

# Display current
print("Current (I) =", current, "Amps")

# Check nature of current
if current < 0.5:
    print("Low current")
elif 0.5 <= current < 2:
    print("Normal current")
else:
    print("High current")