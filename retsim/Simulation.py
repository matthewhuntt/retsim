import pandas as pd
import os
from datetime import date
#from .Retiree import Retiree
from .FixedAccount import FixedAccount
from .Alternative import Alternative
from .Retiree import Retiree

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

        self.fixed_accounts_filepath = os.path.join(self.inputs_folderpath, self.fixed_accounts_filename)
        self.variable_accounts_filepath = os.path.join(self.inputs_folderpath, self.variable_accounts_filename)
        self.retirees_filepath = os.path.join(self.inputs_folderpath, self.retirees_filename)

        #self.fixed_accounts = self.init_fixed_accounts()
        
        self.accounts_matrix = self.generate_accounts_matrix()
        self.retirees_matrix = self.generate_retirees_matrix()
        self.alternatives_dict = self.generate_alternatives_dict()

    def generate_accounts_matrix(self):
        
        
        fixed_accounts = []
    
    def generate_retirees_matrix(self):
        with open(self.retirees_filepath) as f:
            retirees = pd.read_csv(f)
            retiree_a = retirees.iloc[0]
            retiree_b = retirees.iloc[1]

        retirees_matrix = []
        for age_a in range(retiree_a['earliest_retirement_t'], retiree_a['latest_retirement_t'] + 1, 12):
            for age_b in range(retiree_b['earliest_retirement_t'], retiree_b['latest_retirement_t'] + 1, 12):
                retirees_matrix.append((
                    Retiree(id=0, name=retiree_a['name'], retirement_t=age_a), 
                    Retiree(id=1, name=retiree_b['name'], retirement_t=age_b)
                ))

        return retirees_matrix

    def generate_alternatives_dict(self):
        pass

    def run(self):
        pass