#Input we need for users 
#Total rent 
# Total food ordered for snacking
#Electricity units spend
# Charge per unit 

# Output
# Total amount you have to pay is 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in that flat/hostel ="))

total_power = electricity_spend * charge_per_unit

output = (rent + food + total_power) // persons
print("Each person will pay : ",output)




