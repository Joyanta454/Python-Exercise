

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
city = input("Enter city name:").lower()

if city in bangladesh:
    print(f"{city.capitalize()} is in Bangladesh")
elif city in india:
    print(f"{city.capitalize()} is in India")
elif city in pakistan:
    print(f"{city.capitalize()} is in Pakistan")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
city1 = input("Enter city name: ").lower()
city2 = input("Enter another city name: ").lower()
if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in india and city2 in bangladesh:
    print("Both cities are in Bangladesh")
elif city1 in india and city2 in pakistan:
    print("Both cities are in Pakistan")
else:
    print("They don't belong to same country")






