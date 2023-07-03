print("Enter the ammount you want to borrow")
loan_ammount = int(input())
interest_rate = 0.2

print("""For how long do you want to borrrow the loan;
 specify eg. 1 - 1 years;
 2 - 2 years
 3 - 3 years""")
loan_duration_in_years = int(input())

#calculating  number of payment
number_of_payement = loan_duration_in_years * 12

monthly_payment = loan_ammount * interest_rate * (1 + interest_rate ) * number_of_payement \
     / ((1 + interest_rate) * number_of_payement -1)
print(monthly_payment)


