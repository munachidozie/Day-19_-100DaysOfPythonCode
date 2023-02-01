print("== Loan Calculator ==")
print()
money = int(input("How much loan is it?  "))
years = int(input("How many years will it take to repay the loan?  "))
tax = int(input("How much is the APR?  "))
print("$", money, "over", years, "year(s) at", tax, "%", "APR")

for i in range(years):
  money +=(money*(tax/100))
  print("Year", i+1, "is", round(money,2))
print ("You'll pay", round(money,2), "loan")