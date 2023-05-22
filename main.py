import requests
import time

resp = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
categories = []
categories_file = open("categories.json", 'w')
categories_file.write(resp.text)
categories_file.close()
resp = resp.json()['categories']

for re in resp:
  categories.append(re['strCategory'])

print(categories)

ids = []
i = 0
for category in categories:
  url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
  meals = requests.get(url).json()['meals']
  for meal in meals:
    ids.append(meal['idMeal'])

  time.sleep(3)
  i+= 1
  print(i)

written_data = '\n'.join(ids)
ids_file = open('ids.txt', 'w')
ids_file.write('\n'.join(ids))
ids_file.close()