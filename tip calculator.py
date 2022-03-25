print("Welcome to the tip calculator\n")
bill = float(input("What was total Bill?\n$"))
percent = float(input("What percentage of tip you would like to give?\n"))
people = int(input("How many people split the bill?\n"))
pay_tip = (bill + ((bill*percent/100)))/people
print("Each person should pay $",round(pay_tip,2))
