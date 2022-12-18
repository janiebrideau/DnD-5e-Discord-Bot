import json

#TODO: Clean this up. Functional for now.

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
	
	desc_text = ""
	name_text = ""
	range_text = ""
	concentration_text = ""
	duration_text = ""
	high_lvl_string = ""
	
	if descr == True:
		description = json.dumps(json_data['desc']).strip('[]').strip('""')
		desc_text = "\nDESCRIPTION: "

	if name == True:
		name_text = json.dumps(json_data['name']).strip('""')
		name = "NAME: "
		
	if range == True:
		range = json.dumps(json_data['range']).strip('""')
		range_text = "\nRANGE: "
		
	if concentration == True:
		concentration = json.dumps(json_data['concentration']).strip('""')
		concentration_text = "\nCONCENTRATION: "
		
	if duration == True:
		duration = json.dumps(json_data['duration']).strip('""')
		duration_text = "\nDURATION: "
		
	if higher_lvl == True:
		higher_lvl =  json.dumps(json_data['higher_level']).strip('[]').strip('""')
		if len(higher_lvl) != 0:
			high_lvl_string = "\nHIGHER LEVEL: "
		else:
			high_lvl_string = ""
	else:
		higher_lvl - ""

	spell_info = name + name_text + desc_text + description + range_text + range + concentration_text + concentration + duration_text + duration + high_lvl_string + higher_lvl

	return(spell_info)
