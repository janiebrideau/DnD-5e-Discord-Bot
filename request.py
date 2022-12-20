import requests
import json
from config import Values
from parsed_values import returned_values

#We are using https://www.dnd5eapi.co/ API
def spells(name):
	api_response = requests.get("https://www.dnd5eapi.co/api/spells/"+name)
	json_data = json.loads(api_response.text)
	return returned_values(json_data, Values.name, Values.desc, Values.range, Values.concentration, Values.duration, Values.higher_level)

	
