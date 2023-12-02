from datetime import datetime

class MutualFundProfitCalculator:
    def __init__(self, scheme_code, purchase_date, redemption_date, capital=1000000.0, nav_data=None):
        self.scheme_code = scheme_code
        self.purchase_date = datetime.strptime(purchase_date, '%d-%m-%Y')
        self.redemption_date = datetime.strptime(redemption_date, '%d-%m-%Y')
        self.capital = capital
        self.nav_data = nav_data # Assuming nav_data is a dictionary with dates as keys and NAV values as values

    def calculate_units_allotted(self, purchase_date):
        if purchase_date not in self.nav_data:
            raise ValueError(f"NAV data not available for the purchase date: {purchase_date}")

        nav_on_purchase_date = self.nav_data[purchase_date]
        units_allotted = self.capital / nav_on_purchase_date
        return units_allotted

    def calculate_profit(self):
        # Assuming a simple profit calculation for demonstration purposes
        # You may need to replace this with your actual profit calculation logic
        return (self.capital * 0.05) # 5% profit for demonstration

# Example usage
scheme_code = "ABC123"
purchase_date = "26-07-2023"
redemption_date = "01-01-2023"
nav_data = {"26-07-2023": 3682.28990} # Replace with your actual NAV data

calculator = MutualFundProfitCalculator(scheme_code, purchase_date, redemption_date, nav_data=nav_data)
units_allotted = calculator.calculate_units_allotted(purchase_date)

print(f"Number of units allotted on {purchase_date}: {units_allotted:.2f} units")