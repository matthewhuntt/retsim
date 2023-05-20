
class VariableAccount(object):
    def __init__(
            self,
            name: str,
            starting_amount: float,
            taxable: bool,
            active: bool = False,
            monthly_contribution_amount: float = 0
        ) -> None:
        
        self.name = name
        self.cash_flows = self.generate_cash_flows()

    def generate_cash_flows(self):
        pass