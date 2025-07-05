# Basic Currency Converter (No API, Many Countries)

# Static exchange rates (1 USD equals X units of currency)
exchange_rates = {
    'USD': 1.00,    # US Dollar
    'EUR': 0.92,    # Euro
    'GBP': 0.79,    # British Pound
    'INR': 83.3,    # Indian Rupee
    'JPY': 159.5,   # Japanese Yen
    'CAD': 1.36,    # Canadian Dollar
    'AUD': 1.51,    # Australian Dollar
    'CHF': 0.89,    # Swiss Franc
    'CNY': 7.25,    # Chinese Yuan
    'AED': 3.67,    # UAE Dirham
    'SAR': 3.75,    # Saudi Riyal
    'PKR': 278.0,   # Pakistani Rupee
    'BDT': 117.8,   # Bangladeshi Taka
    'ZAR': 18.1,    # South African Rand
    'RUB': 89.0,    # Russian Ruble
    'SGD': 1.35,    # Singapore Dollar
    'HKD': 7.83     # Hong Kong Dollar
}

def convert_currency(amount, from_currency, to_currency):
    # Check if both currencies are supported
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("One or both of the currencies are not supported.")
        return None

    # --- Formula 1: Convert from 'from_currency' to USD ---
    # amount_in_usd = amount / exchange_rates[from_currency]
    # Why? Because exchange_rates[from_currency] tells how many units of 'from_currency' equal 1 USD

    amount_in_usd = amount / exchange_rates[from_currency]

    # --- Formula 2: Convert from USD to 'to_currency' ---
    # converted_amount = amount_in_usd * exchange_rates[to_currency]
    # Why? Because exchange_rates[to_currency] tells how many units of 'to_currency' equal 1 USD

    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return converted_amount

# -------- Program Starts --------
print("Welcome to the Traditional Currency Converter!\n")

print("Supported currencies:")
print(', '.join(exchange_rates.keys()))
print()

amount = float(input("Enter the amount: "))
from_curr = input("From currency (e.g., USD, EUR, INR): ").upper()
to_curr = input("To currency (e.g., USD, EUR, INR): ").upper()

converted = convert_currency(amount, from_curr, to_curr)

if converted is not None:
    print(f"\n{amount} {from_curr} = {converted:.2f} {to_curr}")
