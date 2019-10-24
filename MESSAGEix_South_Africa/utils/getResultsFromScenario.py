def getResultsFromScenario(Model, name):
	emissions = Model.var('EMISS')
	act = Model.var('ACT')
	cap = Model.var('CAP')
	cap_new = Model.var('CAP_NEW')
	stock = Model.var('STOCK')
	capacity_new = Model.var('CAP_NEW')
	land = Model.var('LAND')
	rel = Model.var('REL')
	demand = Model.var('DEMAND')
	price_commodity	= Model.var('PRICE_COMMODITY')
	price_emission = Model.var('PRICE_EMISSION')
	cost_nodal = Model.var('COST_NODAL')
	cost_nodal_net = Model.var('COST_NODAL_NET')
	gdp = Model.var('GDP')
	i = Model.var('I')
	c = Model.var('C')
	
	ScenarioSpecificResults = ScenarioResults(name, emissions, act, cap, cap_new, stock, land, rel, demand, price_commodity,price_emission,cost_nodal,cost_nodal_net, gdp,i,c)
	return ScenarioSpecificResults

class ScenarioResults:
	def __init__(self, name, emissions, act, cap, cap_new, stock, land, rel, demand, price_commodity,price_emission,cost_nodal,cost_nodal_net, gdp,i,c):
		self.name = name
		self.emissions = emissions
		self.capacity = cap
		self.activity = act
		self.stock = stock
		self.capacity_new = cap_new
		self.land = land
		self.rel = rel
		self.demand = demand
		self.price_commodity = price_commodity
		self.price_emission = price_emission
		self.cost_nodal = cost_nodal
		self.cost_nodal_net = cost_nodal_net
		self.gdp = gdp
		self.i = i
		self.c = c
		
		#array(['OBJ', 'EXT', 'STOCK', 'CAP_NEW', 'CAP', 'ACT', 'EMISS', 'LAND',
		#'REL', 'DEMAND', 'PRICE_COMMODITY', 'PRICE_EMISSION', 'COST_NODAL',
		#'COST_NODAL_NET', 'GDP', 'I', 'C'], dtype='<U15')