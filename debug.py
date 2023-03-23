from lib.funding_round import *
from lib.venture_capitalist import *
from lib.startup import *

# code here
# e.g.
# 
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
s2 = Startup( 'Yummy', 'Matthias Miler', 'www.mm.com' )
s3 = Startup( 'Cool Vibes', 'Cody Viper', 'www.viper.com' )


vc1 = VentureCapitalist( 'Peter Gregory', 4000000000 )
vc2 = VentureCapitalist( 'David D', 2000000000 )
vc3 = VentureCapitalist( 'Sheldon Cooper', 120000000 )


fr1 = FundingRound( s1, vc2, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( s2, vc2, 'Pre-Seed', 200000.00 )
fr3 = FundingRound( s3, vc3, 'Pre-Seed', 400000.50 )







# do not remove
import ipdb; ipdb.set_trace()
