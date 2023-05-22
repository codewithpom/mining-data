import time
import requests
import json
ids = open('ids.txt').read().split("\n")
meals = {
  "meals": []
}

for id in ids:
  url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
  print(id)
  meal = requests.get(url).json()
  meals['meals'].append(meal['meals'][0])
  time.sleep(2)
 
print(json.dumps(meals), file=open('meals.json', 'w'))

