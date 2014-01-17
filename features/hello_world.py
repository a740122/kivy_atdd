import json 
import requests
from lettuce import *

@step('the application is running')
def application_is_running(step):
  return

@step('I should see "(.*?)"')
def i_should_see_message(step, expected):
  response = requests.get('http://localhost:5000/ui')
  ui_tree = response.json()#json.loads(response.json())
  label = search_by_id(ui_tree, 'mylabel')
  assert label['value'] == expected

def search_by_id (root, id):
  for child in root['children']:
    if child['id'] == id: 
      return child
    return search_by_id(child, id)
