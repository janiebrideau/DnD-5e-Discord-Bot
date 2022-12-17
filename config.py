#Set which value you want returned from the API

def config_all():
	config_all = False
	return(config_all)

def config():
	desc = True
	name = True
	range = False
	concentration = True
	duration = True
	higher_level = False
	return (desc, name, range, concentration, duration, higher_level)