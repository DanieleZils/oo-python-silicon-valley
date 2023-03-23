from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:

    all = []

    def __init__(self, name, total_worth ):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

#     VentureCapitalist.tres_commas_club`
#   - returns an list of all venture capitalist instances in the Trés Commas club (they have more then 1,000,000,000 `total_worth`)

    @classmethod
    def tres_commas_club(cls):
        return [ v for v in cls.all if v.total_worth > 1000000000]
    
#     `VentureCapitalist#offer_contract`
#   - given a **startup object**, type of investment (as a string),
# and the amount invested (as a float), creates a new funding round and associates it 
# with that startup and venture capitalist.

    def offer_contract(self, startup, type, investment_amount:float):
        FundingRound(self, startup, type, investment_amount )

#         VentureCapitalist#funding_rounds`
#   - returns an list of all funding rounds for that venture capitalist
    @property
    def num_funding_rounds(self):
        return [f for f in FundingRound.all if f.venture_capitalist == self]

# - `VentureCapitalist#portfolio`
#   - Returns a **unique** list of all startups this venture capitalist has funded

    @property
    def portfolio(self):
        return list ( {f.startup for f in self.num_funding_rounds} )
    
#      `VentureCapitalist#biggest_investment`
#   - returns the largest funding round given by this venture capitalist


    @property
    def biggest_investment(self):
        big_investment = 0
        
        for f in self.num_funding_rounds:
            if f.investment_amount >= big_investment:
              big_investment = f.investment_amount
              return f.investment_amount
            
# `VentureCapitalist#invested`
#   - given a **domain string**, 
# returns the total amount invested in that domain

    def invested(self, domain):
        return [f.investment_amount for f in self.num_funding_rounds if f.startup.domain == domain]
