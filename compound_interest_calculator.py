principal = int(input("enter your principal: "))
user_rate = int(input("enter your rate: ))
rate = float(user_rate / 100)
years = int(input("enter number of years: ")) 

amount = principal * (1 * rate)**years
print(amount)
