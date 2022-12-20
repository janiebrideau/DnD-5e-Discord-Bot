import requests
import json
from config import Values
from parsed_values import parsed_response

#We are using https://www.dnd5eapi.co/ API
def spells(name):
	api_response = requests.get("https://www.dnd5eapi.co/api/spells/"+name)
	json_data = json.loads(api_response.text)
	return parsed_response(json_data, Values.name, Values.desc, Values.range, Values.concentration, Values.duration, Values.higher_level)

	
