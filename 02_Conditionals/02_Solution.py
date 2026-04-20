# 2. Movie Ticket Pricing
# Movie tickets are priced based on age: $12 for adults (13+), $8 for children (12 and under). Senior citizens (65+) get a discount of $2.

age = 65
day = "Wednesday"

if age < 13:
    price = 8
elif age < 65:
    price = 12
else:
    price = 10

if day == "Wednesday":
    price -= 2

print(f"Ticket price for a {age}-year-old on {day}: ${price}")

## OR 

age = 6
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)