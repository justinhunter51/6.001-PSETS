def twelveMonthPayoff(balance, annualInterestRate):
  monthlyPayment = 10
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