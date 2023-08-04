import os
import time
from replit import db
from embedchain import App

chat_with_web_app = App()

file_list = os.listdir("docs")

while True:
  os.system("clear")
  input_query = input("\nAsk your question: ")
  answer = chat_with_web_app.query(input_query)
  print(f"Answer: {answer}\n\n")
  input("Press any key to ask another question >")