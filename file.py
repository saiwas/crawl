import os

def create_file(file_name, file_content):
  path = os.path.abspath('.') + "/data/" + file_name
  print(path)
  file = open(path, "w")
  file.write(file_content)
  file.close()
