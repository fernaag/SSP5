def getResultsFromScenario(Model):
	emissions = Model.var('EMISS')
	act = Model.var('ACT')
	cap = Model.var('CAP')
	
	ScenarioSpecificResults = ScenarioResults(emissions, act, cap)
	return ScenarioSpecificResults

class ScenarioResults:
	def __init__(self, name, emissions, act, cap, cap_new, stock, land, rel, ):
		self.name = name
		self.emissions = emissions
		self.capacity = cap
		self.activity = act
		self.stock = stock
		self.capacity_new = cap_new
		self.land = land
		self.rel = rel
		
		#array(['OBJ', 'EXT', 'STOCK', 'CAP_NEW', 'CAP', 'ACT', 'EMISS', 'LAND',
		#'REL', 'DEMAND', 'PRICE_COMMODITY', 'PRICE_EMISSION', 'COST_NODAL',
		#'COST_NODAL_NET', 'GDP', 'I', 'C'], dtype='<U15')