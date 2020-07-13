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


  
