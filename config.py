#Set which value you want returned from the API

#If you want all values to be desplayed, set this to True.
def config_all():
	config_all = True
	return(config_all)

#If config_all is set to false, it will look at which value to return, set them to True or False accordingly.
def config():
	desc = True
	name = True
	range = False
	concentration = True
	duration = True
	higher_level = True
	return (desc, name, range, concentration, duration, higher_level)