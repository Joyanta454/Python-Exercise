# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street = 'Kalitola, Naogaon Sadar'
city = 'Naogaon'
country = 'Bangladesh'
#using + operator to 
address= street + "\n" + city + "\n" + country
print(address)
  #using f-string
print("With f-string")
address_fstring = f"{street}\n{city}\n{country}"
print(address_fstring)
# Create a variable to store the string "Earth revolves around the sun"

string = 'Earth revoles around the sun'
#  i.Print "revolves" using slice operator
print(string[5:13])

#  ii.Print "sun" using negative index
print(string[-3:])

# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
fruitCount = 6
veggiesCount = 8
print("I eat {} veggies and {} fruits daily".format(fruitCount, veggiesCount))

# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s='maine 200 banana khaye'
s = s.replace('200', '10').replace('banana', 'samosa')
print(s)