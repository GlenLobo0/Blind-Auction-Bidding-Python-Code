print("Welcome to the Tip calculator")
bill =float(input("How much was the bill:$"))
tip =int(input("What amount of percentaage would you like to give for ur food(10,20,30):"))
people=int(input("how many people are there to split up with: "))
bill_withtip = bill*(tip/100) + bill
divide_withpeople =bill_withtip/people
roundup=round(divide_withpeople, 2)
print(f"Each of yáll(or your lonely ass) has/have to pay ${roundup}")
