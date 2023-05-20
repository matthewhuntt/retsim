
class FixedAccount(object):
    def __init__(
            self,
            name: str,
            monthly_amount: float,
            start_t: int,
            end_t: int,
            taxable: bool,
            option_group: int, #defines a group of options for the same account, only one option may be selected
        ) -> None:
        
        self.name = name
        self.mothly_amount = monthly_amount
        self.start_t = start_t
        self.end_t = end_t
        self.taxable = taxable
        self.option_group = option_group
        self.cash_flows = generate_cash_flows()

    def generate_cash_flows(self):
        return [CashFlow(amount=self.monthly_amount, t=t, account=self) for t in range(self.start_t, self.end_t)]