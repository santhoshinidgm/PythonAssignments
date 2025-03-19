# Currency conversion rates (example rates)
exchange_rates = {
    "USD": 1,       # Base currency
    "INR": 83.2,    # 1 USD = 83.2 INR
    "EUR": 0.91,    # 1 USD = 0.91 EUR
    "JPY": 150.5,   # 1 USD = 150.5 JPY
    "GBP": 0.78     # 1 USD = 0.78 GBP
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency"
    
    # Convert to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return round(converted_amount, 2)

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("Enter from currency (USD, INR, EUR, JPY, GBP): ").upper()
to_currency = input("Enter to currency (USD, INR, EUR, JPY, GBP): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")
