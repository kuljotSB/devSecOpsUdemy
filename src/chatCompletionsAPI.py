#importing importing libraries
import os
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv

def chat_completions_api(user_query: str):
  load_dotenv()
  azure_endpoint = os.getenv("OPENAI_API_BASE")
  azure_key = os.getenv("OPENAI_API_KEY")
  chat_model = os.getenv("OPENAI_CHAT_MODEL")

  client = AzureOpenAI(
    azure_endpoint = azure_endpoint, 
    api_key=azure_key,  
    api_version="2024-02-15-preview"
  )

  #send request to Azure OpenAi model
  response = client.chat.completions.create(
      model=chat_model, # model = "deployment_name".
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": user_query}
      ]
  )

  #printing the final response after making the API call
  print("the information is:" + response.choices[0].message.content + "\n")
  
  
  
  return response.choices[0].message.content