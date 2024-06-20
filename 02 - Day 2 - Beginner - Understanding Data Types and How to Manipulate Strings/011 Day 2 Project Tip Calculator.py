#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

'''
Welcome to the tip calculator!
What was the total bill? $
150
How much tip would you like to give? 10, 12, or 15? 
12
How many people to split the bill?
5
Each person should pay: $33.60'''

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
person=int(input("How many people to split the bill?"))
#ans= ((tip/100)+bill)/person
ans = (bill/person)*(tip/100+1)
final_ans = round(ans,2)
print(f"final ans is {final_ans:.2f}")