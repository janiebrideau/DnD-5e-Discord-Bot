import json
import logging

def returned_values(json_data, name, desc, range, concentration, duration, higher_lvl):

	if desc == True:
		desc_response = json.dumps(json_data['desc']).strip('[]').strip('""')
		desc_text = "\nDESCRIPTION: "
	else:
		desc_response = ""
		desc_text = ""

	if name == True:
		name_response = json.dumps(json_data['name']).strip('""')
		name_text = "NAME: "
	else:
		name_response = ""
		name_text = ""
		
	if range == True:
		range_response = json.dumps(json_data['range']).strip('""')
		range_text = "\nRANGE: "
	else:
		range_response = ""
		range_text = ""
		
	if concentration == True:
		concentration_response = json.dumps(json_data['concentration']).strip('""')
		concentration_text = "\nCONCENTRATION: "
	else:
		concentration_response = ""
		concentration_text = ""
		
	if duration == True:
		duration_response = json.dumps(json_data['duration']).strip('""')
		duration_text = "\nDURATION: "
	else:
		duration_response = ""
		duration_text = ""

	if higher_lvl == True:
		higher_lvl_response =  json.dumps(json_data['higher_level']).strip('[]').strip('""')
		if len(higher_lvl_response) != 0:
			high_lvl_string = "\nHIGHER LEVEL: "
		else:
			high_lvl_string = ""
	else:
		higher_lvl_response = ""
		high_lvl_string = ""

	spell_info = name_text + name_response + desc_text + desc_response + range_text + range_response + concentration_text + concentration_response + duration_text + duration_response + high_lvl_string + higher_lvl_response

	if not spell_info:
		logging.error('spell_info is empty. Make sure config.py is set up properly.')
	
	return(spell_info)
