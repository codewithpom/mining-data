import json
import os
import threading
import time



def execute_command(command):
  os.system(command)
  return

meals = json.loads(open('categories.json').read())['categories']

threads = []

for meal in meals:
  print(meal['strCategoryThumb'])
  url = meal['strCategoryThumb']
  command = f'curl "{url}" > "images/categories/' + url.split(r"/")[-1] + '" --silent'
  print(command)
  thread = threading.Thread(target=execute_command, args=(command,))
  threads.append(thread)
  thread.start()

for thread_ in threads:
  while True:
    try:
      thread_.join()

    except Exception:
      time.sleep(1)
      continue

print('DONE!!')

