from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:

    all = []


    def __init__(self, name, founder, domain):
        self.name = name
        self._founder = founder
        self._domain = domain
        Startup.all.append(self)
    
    @property
    def founder(self):
        return self._founder
    
    @property
    def domain(self):
        return self._domain


# Startup#pivot`
#   - given a string of a **domain** and a string 
# of a **name**, change the domain and name of the startup. 
# This is the only public method through which the domain can be changed.

    def pivot(self, new_domain, new_name):
        self._domain = new_domain
        self.name = new_name


# Startup.find_by_founder`
#   - given a string of a **founder's name**, returns the **first startup instance** whose founder's name matches


    @classmethod
    def find_by_founder(cls, founder):
        return [s for s in cls.all if s.founder == founder ]
    
#     - `Startup.domains`
#   - should return an **list** of all of the different startup domains

    @classmethod
    def domains(cls):
        return [s.domain for s in cls.all]
    
# - `Startup#sign_contract`
#   - given a **venture capitalist object**, type of investment (as a string), 
# and the amount invested (as a float), creates a new funding round 
# and associates it with that startup and venture capitalist.

    def sign_contract(self, venture_capitalist, type, investment_amount:float):
        FundingRound(self, venture_capitalist, type, investment_amount)

#         `Startup#num_funding_rounds`
#   - Returns the total number of funding rounds that the startup has gotten

    @property
    def num_funding_rounds(self):
        return [f for f in FundingRound.all if f.startup == self]
    
#     - `Startup#total_funds`
#   - Returns the total sum of investments that the startup has gotten

    @property
    def total_funds(self):
        return sum (f.investment_amount for f in self.num_funding_rounds)

#  Returns a **unique** list of all the venture capitalists that have invested in this company

    @property
    def investors(self):
        return list ( {f.venture_capitalist for f in self.num_funding_rounds} )
    
#      `Startup#big_investors`
#   - Returns a **unique** list of all the venture capitalists that have invested in this company and are in the Trés Commas club

    @property
    def big_investors(self):
        return list ({ venture_capitalist for venture_capitalist in self.investors if venture_capitalist.total_worth > 1000000000})