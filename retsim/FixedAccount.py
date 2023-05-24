from .CashFlow import CashFlow
from datetime import date
from datetime import datetime
import math
import numpy as np

class FixedAccount(object):
    def __init__(
            self,
            alt,
            name: str,
            monthly_amount: float,
            retiree_id: int,
            start_date: str,
            end_date: str,
            taxable: bool,
            option_group: int, #defines a group of options for the same account, only one option may be selected
        ) -> None:
        
        self.alt = alt
        self.name = name
        self.monthly_amount = monthly_amount
        self.retiree_id = retiree_id
        self.start_date = start_date
        self.end_date = end_date
        self.taxable = taxable
        self.option_group = option_group

        self.start_t = self.calculate_start_t()
        self.end_t = self.calculate_end_t()

        self.cash_flows = self.generate_cash_flows()

    def calculate_start_t(self):
        if self.start_date == '<retirement_t>':
            return self.alt.retirees_dict[self.retiree_id].retirement_t
        elif self.start_date == '<today>':
            return 0
        elif datetime.strptime(self.start_date, "%m/%d/%Y").date() <= date.today():
            return 0
        else:
            return (datetime.strptime(self.start_date, "%m/%d/%Y").date() - date.today()).days
    
    def calculate_end_t(self):
        if self.end_date == '<retirement_t>':
            return self.alt.retirees_dict[self.retiree_id].retirement_t
        elif math.isnan(self.end_date):
            return 1000
        elif self.start_date == '<today>':
            return 0
        else:
            print("about to convert: {}, {}".format(self.end_date, type(self.end_date)))
            return (datetime.strptime(self.start_date, "%m/%d/%Y").date() - date.today()).days

    def generate_cash_flows(self):
        return [CashFlow(amount=self.monthly_amount, t=t, account=self) for t in range(self.start_t, self.end_t)]
    