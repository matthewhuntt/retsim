from .CashFlow import CashFlow
from datetime import date
import math

class FixedAccount(object):
    def __init__(
            self,
            name: str,
            monthly_amount: float,
            start_date: date,
            end_date: date,
            taxable: bool,
            option_group: int, #defines a group of options for the same account, only one option may be selected
        ) -> None:
        
        self.name = name
        self.monthly_amount = monthly_amount
        self.start_date = start_date
        self.end_date = end_date
        self.taxable = taxable
        self.option_group = option_group

        self.start_t = self.calculate_start_t()
        self.end_t = self.calculate_end_t()

        self.cash_flows = self.generate_cash_flows()

    def calculate_start_t(self):
        if self.start_date <= date.today():
            return 0
        else:
            return (self.start_date - date.today()).days
    
    def calculate_end_t(self):
        if self.end_date is None:
            return 1000
        else:
            return (self.end_date - date.today()).days
        
    def generate_cash_flows(self):
        return [CashFlow(amount=self.monthly_amount, t=t, account=self) for t in range(self.start_t, self.end_t)]
    