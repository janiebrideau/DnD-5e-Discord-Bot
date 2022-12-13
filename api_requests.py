import requests
import json

#We are using https://www.dnd5eapi.co/ API
#API Request for Spells - hard coded for now just to test
def spells():
  api_response = requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow")
  json_data = json.loads(api_response.text)
  return(json_data)