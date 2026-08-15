funding_request = int(input("Requested Funding Amount? $"))
payments = int(input("How many payments? "))
payment_freq = input("Daily(d)? Weekly(w)? or Monthly(m)? ")
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

payment_freq = input("Daily(d)? Weekly(w)? or Monthly(m)? ")

print("Term:", term, " months")

print("Buy Rate: ", buy_rate)

factor = buy_rate + upsell
print("Factor: ", factor)

print(f"Origination Fee: ${origination_fee:,.2f}")

payback_amt = factor * funding_request
payment_amt = payback_amt / payments

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