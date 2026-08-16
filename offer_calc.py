def calculate_factor(buy_rate, upsell):
    return buy_rate + upsell
def calculate_payback(funding_request, factor):
    return funding_request * factor
def calculate_payment(payback_amount, payments):
    return payback_amount / payments

funding_request = int(input("Requested Funding Amount? $"))
while True:
    payments = int(input("How many payments? "))
    if payments > 0:
        break
    print("There are not enough payments to repay the loan! Please try again.")
while True:
    payment_freq = input("Daily(d)? Weekly(w)? or Monthly(m)? ").lower()
    if payment_freq in ("d", "w", "m"):
        break
    print("Please enter d, w, or m.")
buy_rate = float(input("What is the Buy Rate? "))
upsell = float(input("Upsell = (Factor Rate) - (Buy Rate)? "))
origination = float(input("% Origination Fee? "))
origination_fee = origination * funding_request * 0.01

print()
print("Offer Calculator")
print("--------------------")
print(f"Requested Funding Amount: ${funding_request:,.2f}")
print("Number of payments:", payments)
print("Payment Frequency:", payment_freq)

if payment_freq == "d":
    term = payments / 20
elif payment_freq == "w": 
    term = payments / 4
elif payment_freq == "m": 
    term = payments / 1

print("Term:", term, " months")

print("Buy Rate: ", buy_rate)

factor = calculate_factor(buy_rate, upsell)
print("Factor: ", factor)

print(f"Origination Fee: ${origination_fee:,.2f}")

payback_amt = calculate_payback(funding_request, factor)
payment_amt = calculate_payment(payback_amt, payments)

print(f"Payback Amount: ${payback_amt:,.2f}")
print(f"Payment Amount: ${payment_amt:,.2f}") 
if payment_freq == "d":
 print ("daily payments")
elif payment_freq == "w":
 print ("weekly payments")
elif payment_freq == "m":
 print ("monthly payments")

net_funding = funding_request - origination_fee
print(f"Net Funding: ${net_funding:,.2f}")