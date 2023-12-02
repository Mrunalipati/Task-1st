from datetime import datetime
from dateutil.parser import parse

class MutualFundProfitCalculator:
    def __init__(self):
        # Assume that the mutual fund NAV data is available as a dictionary
        # where keys are date strings and values are NAV prices.
        self.nav_data = {
            "01-01-2023": 15.0,
            "02-01-2023": 15.5,
            # Add more date-NAV pairs as needed
        }

    def calculate_profit(self, scheme_code, start_date, end_date, capital=1000000.0):
        start_date = parse(start_date, dayfirst=True)
        end_date = parse(end_date, dayfirst=True)

        if start_date > end_date:
            raise ValueError("Start date cannot be later than end date.")

        start_nav = self.nav_data.get(start_date.strftime("%d-%m-%Y"))
        end_nav = self.nav_data.get(end_date.strftime("%d-%m-%Y"))

        if start_nav is None or end_nav is None:
            raise ValueError("NAV data not available for specified dates.")

        units_purchased = capital / start_nav
        redemption_amount = units_purchased * end_nav
        profit = redemption_amount - capital

        return profit

# Example usage:
calculator = MutualFundProfitCalculator()
profit = calculator.calculate_profit("ABC123", "01-01-2023", "02-01-2023", capital=1000000.0)
print(f"Profit: {profit:.2f} INR")
