## Inputs we need to get from the user
# Total rent 
# Electricity bill
# Charge par unit

## Output
# Total amount you've to pay is

rent = int(input("Enter your hostal/flat rent: "))
food = int(input("Enter your food ordered: "))
electricity_spend = int(input("Enter your electricity spend: "))
charge_per_unit = int(input("Enterthe charge per unit: "))
persons = int(input("Enter the number of persons living in room/flat: "))

total_bill = electricity_spend * charge_per_unit

output  = rent + food + total_bill
print("Each person has to pay: ",output/persons)
