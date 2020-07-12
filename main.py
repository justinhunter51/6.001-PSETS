#To help you get started, here is a rough outline of the stages you should probably follow in writing your code:

#Compute the monthly payment, based on the previous month’s balance.

#Update the outstanding balance by removing the payment, then charging interest on the result.

#Output the month, the minimum monthly payment and the remaining balance.

#Keep track of the total amount of paid over all the past months so far.

#Print out the result statement with the remaining balance.

# Test Case 1:
balance = 42 
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def cardInterest(balance, annualInterestRate, monthlyPaymentRate):
  paid = 0
  previousBalance = balance 

  for i in range(12):
    monthlyPayment = previousBalance * monthlyPaymentRate
    paid += monthlyPayment
    previousBalance -= monthlyPayment
    previousBalance = (previousBalance + ((annualInterestRate / 12) * previousBalance))
    print(previousBalance)

  print("Remaining balance:", round(previousBalance, 2))
  


cardInterest(balance, annualInterestRate, monthlyPaymentRate)