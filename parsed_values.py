import json

def returned_values_all(json_data):
	description = json.dumps(json_data['desc']).strip('[]').strip('""')
	name = json.dumps(json_data['name']).strip('""')
	range = json.dumps(json_data['range']).strip('""')
	concentration = json.dumps(json_data['concentration']).strip('""')
	duration = json.dumps(json_data['duration']).strip('""')
	higher_level =  json.dumps(json_data['higher_level']).strip('[]').strip('""')

	#This is often empty for certain spells. Make it not show up if it is empty.
	high_lvl_string = ""
	if len(higher_level) != 0:
		high_lvl_string = "\nHIGHER LEVEL: "

	spell_info = "NAME: " + name + "\nDESCRIPTION: " + description + "\nRANGE: " + range + "\nCONCENTRATION: " + concentration + "\nDURATION: " + duration + high_lvl_string + higher_level

	return(spell_info)

def returned_values(json_data, descr, name, range, concentration, duration, higher_lvl):
	return("TO DO.")

		