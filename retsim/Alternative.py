import pandas as pd
from datetime import date

from .FixedAccount import FixedAccount

class Alternative(object):
    def __init__(
            self,
            sim,
            retirement_t_dict,
        ) -> None:
        
        self.sim = sim
        self.retirement_t_dict = retirement_t_dict

        self.fixed_accounts = self.init_fixed_accounts()
        self.variable_accounts = self.init_variable_accounts()
        self.accounts = self.fixed_accounts + self.variable_accounts

        self.aggregate_cash_flows = self.get_aggregate_cash_flows()

    def generate_accounts(self):
        pass

    def init_fixed_account(self, account_row):
        return FixedAccount(
            alt=self,
            name=account_row['name'],
            monthly_amount=account_row['monthly_amount'],
            retiree_id=account_row['tied_to_retiree_id'],
            start_date=account_row['start_date'],
            end_date=account_row['end_date'],
            taxable=account_row['taxable_flag'],
            option_group=account_row['option_group']
        )
    
    def init_fixed_accounts(self):
        with open(self.sim.fixed_accounts_filepath) as f:
            fixed_accounts_df = pd.read_csv(f)
        
        return [self.init_fixed_account(account) for (i, account) in fixed_accounts_df.iterrows()]

    def init_variable_accounts(self):
        return []

    def get_aggregate_cash_flows(self):
        aggregate_cash_flows = []
        for account in self.accounts:
            aggregate_cash_flows += account.generate_cash_flows()
        
        return aggregate_cash_flows