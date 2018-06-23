import os
from pathlib import Path

def create_file(file_name, file_content):
  path = os.path.abspath('.') + "/data/" + file_name + ".txt"
  print(path)
  if Path(path).is_file():
    file = open(path, "a")
  else:
    file = open(path, "w")
  file.write(file_content)
  file.write('\n\r')
  file.close()
