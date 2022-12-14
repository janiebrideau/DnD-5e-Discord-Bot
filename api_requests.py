import requests
import json

#We are using https://www.dnd5eapi.co/ API
#API Request for Spells - hard coded for now just to test
def spells(name):
	api_response = requests.get("https://www.dnd5eapi.co/api/spells/"+name)
	json_data = json.loads(api_response.text)
	description = json.dumps(json_data['desc']).strip('[]').strip('""')
	name = json.dumps(json_data['name']).strip('""')
	spell_info = name + ": "+description
	return(spell_info)