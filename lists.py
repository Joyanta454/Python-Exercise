# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

monthly_expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
extra_feb = monthly_expense[1]-monthly_expense[0]
print("{} dollars I sent extra compare to January".format(extra_feb))
# 2. Find out your total expense in first quarter (first three months) of the year.
total_first_quarter = sum(monthly_expense[:3])
print("MY expense in first quarter (first three months) of the year is:{}".format(total_first_quarter))
# 3. Find out if you spent exactly 2000 dollars in any month

for x in monthly_expense:
    if x == 2000:
        print("I spent exactly 2000 dollers in {} month".format(x))
    spent = "No! I exactly not spent 2000 dollers in any month"
print(spent)
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expense.insert(5, 1980)
print("After adding 1980 of June month:",monthly_expense)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expense[3] = monthly_expense[3] - 200
print("Monthly list after correction in my list")
print(monthly_expense)

# You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
print("Length of the list is: ", len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("List after add 'black Panther at the end of the list", heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop(5)
heros.insert(3, "Black Panther")
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]={'doctor strange'}
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)