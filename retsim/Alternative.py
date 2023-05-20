from .FixedAccount import FixedAccount

class Alternative(object):
    def __init__(
            self,
            sim,
            retirement_t_dict,
            accounts,
        ) -> None:
        
        self.sim = sim
        self.retirement_t_dict = retirement_t_dict
        self.accounts = accounts
        self.aggregate_cash_flows = self.get_aggregate_cash_flows()

    def get_aggregate_cash_flows(self):
        aggregate_cash_flows = []
        for account in self.accounts:
            aggregate_cash_flows += account.generate_cash_flows()
        
        return aggregate_cash_flows