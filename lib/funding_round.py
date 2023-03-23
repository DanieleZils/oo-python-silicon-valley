class FundingRound:


    all = []

    def __init__(self, startup, venture_capitalist, type, investment_amount):
        self._startup = startup
        self._vc = venture_capitalist
        self.type = type
        if investment_amount < 0:
           raise ValueError("Investment amount cannot be negative")
        self.investment_amount = float (investment_amount)
        FundingRound.all.append(self)
    

    @property
    def startup(self):
        return self._startup
    
    @property
    def venture_capitalist(self):
        return self._vc
    
    
    