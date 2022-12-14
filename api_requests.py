import requests
import json

#We are using https://www.dnd5eapi.co/ API
#API Request for Spells - hard coded for now just to test
def spells(name):
	api_response = requests.get("https://www.dnd5eapi.co/api/spells/"+name)
	json_data = json.loads(api_response.text)
	
	description = json.dumps(json_data['desc']).strip('[]').strip('""')
	name = json.dumps(json_data['name']).strip('""')
	range = json.dumps(json_data['range']).strip('""')
	concentration = json.dumps(json_data['concentration']).strip('""')
	duration = json.dumps(json_data['duration']).strip('""')
	higher_level =  json.dumps(json_data['higher_level']).strip('[]').strip('""')
	
	spell_info = "NAME: " + name + "\nDESCRIPTION: " + description + "\nRANGE: " + range + "\nCONCENTRATION: " + concentration + "\nDURATION: " + duration + "\nHIGHER LEVEL: " + higher_level
	return(spell_info)