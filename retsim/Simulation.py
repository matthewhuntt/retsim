import pandas as pd

class Simulation(object):
    def __init__(
            self,
            inputs_folderpath: str,
            fixed_accounts_filename: str,
            variable_accounts_filename: str,
            retirees_filename: str,
            iterations = 1,
        ) -> None:
        
        self.inputs_folderpath = inputs_folderpath
        self.fixed_accounts_filename = fixed_accounts_filename
        self.variable_accounts_filename = variable_accounts_filename
        self.retirees_filename = retirees_filename
        self.iterations = iterations

        self.alternatives_dict = self.generate_alternatives_dict()

    def generate_alternatives_dict(self):
        pass

    def run(self):
        pass