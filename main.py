import os
import time
from replit import db


from embedchain import App

chat_with_web_app = App()

import os

file_list = os.listdir("docs")

for filename in file_list:
  keys = db.keys()
  if filename not in keys:
    print("Loading file: " + filename)
    chat_with_web_app.add("pdf_file", f"docs/{filename}")
    db[filename] = None
  else:
    print("File already loaded: " + filename)


while True:
  os.system("clear")
  input_query = input("\nAsk your question: ")
  answer = chat_with_web_app.query(input_query)
  print(f"Answer: {answer}\n\n")
  input("Press any key to ask another question")