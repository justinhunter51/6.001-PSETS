balance = 320000
annualInterestRate = 0.2

#Lowest Payment: 29157.09

#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

def twelveMonthPayoff(balance, annualInterestRate):
  monthlyPaymentLowerBound = balance / 12
  monthlyPaymentUpperBound = (balance x (1 + (annualInterestRate / 12))^12) / 12.0
  while balanceRemaining(monthlyPayment, balance, annualInterestRate) > 0:
    monthlyPayment += 10
  return monthlyPayment

def balanceRemaining(monthlyPayment, balance, annualInterestRate):
  previousBalance = balance
  for i in range (12):
    previousBalance -= monthlyPayment
    previousBalance += (annualInterestRate / 12) * previousBalance
  return previousBalance

print(twelveMonthPayoff(balance, annualInterestRate))




  