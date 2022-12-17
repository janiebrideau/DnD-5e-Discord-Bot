import requests
import json
from config import config_all
from config import config
from parsed_values import returned_values_all
from parsed_values import returned_values

#We are using https://www.dnd5eapi.co/ API
#API Request for Spells - hard coded for now just to test
def spells(name):
	api_response = requests.get("https://www.dnd5eapi.co/api/spells/"+name)
	json_data = json.loads(api_response.text)
	
	if config_all() == True:
		 return returned_values_all(json_data)
	else:
		config_values = config()
		return  returned_values(json_data, config_values[0], config_values[1], config_values[2], config_values[3], config_values[4], config_values[5])

	
