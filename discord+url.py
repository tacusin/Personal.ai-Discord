"""
Discord Bot

Author: Matthew Schafer / VE7LTX
Company: Diagonal Thinking LTD

Description:
This Discord bot interacts with an AI service to generate responses and uploads messages to a memory API. It utilizes the Discord.py library.

Dependencies:
- nextcord (Discord.py) - Library for Discord integration
- requests - Library for making HTTP requests

"""

# Importing necessary modules
import nextcord as discord
import requests
import json
import logging
import os

# Retrieving environment variables
bot_token = os.environ['BOT_TOKEN']
api_key = os.environ['API_KEY']
base_url = os.environ['BASE_URL']
memory_api_url = os.environ['MEMORY_API_URL']
domain_name = os.environ['DOMAIN_NAME']
upload_url = os.environ['UPLOAD_URL']

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Defining intents
intents = discord.Intents.all()
client = discord.Client(intents=intents)

message_memory = ""

# upload url def
def upload_url(url):
    headers = {'Content-Type': 'application/json', 'x-api-key': api_key}
    payload = {
        "Text": url
    }
  
    try:
        response = requests.post(upload_url,
                                 headers=headers,
                                 json=payload,
                                 timeout=60)
        response.raise_for_status()
        response_json = response.json()
        print(f'Memory API response: {json.dumps(response_json, indent=2)}')
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def get_ai_response(message):
  headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

  message_data = {
    'Text': str(message).replace('"', '\\"').replace('\n', ' '),
    "DomainName": domain_name
  }

  try:
    response = requests.post(base_url,
                             headers=headers,
                             json=message_data,
                             timeout=60)
    response.raise_for_status()
    response_json = response.json()
    ai_message = response_json.get('ai_message', '')
    ai_score = response_json.get('ai_score', '')
    return ai_message, ai_score
  except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')
  return 'Sorry, an error occurred while processing your request.', ''


def upload_memory(text, source_name, device_name="API", created_time=None):
  headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

  payload = {
    "Text": text.replace('"', '\\"').replace('\n', ' '),
    "SourceName": source_name,
    "DeviceName": device_name,
    "DomainName": domain_name,
    "CreatedTime": created_time if created_time else None,
  }

  try:
    response = requests.post(memory_api_url,
                             headers=headers,
                             json=payload,
                             timeout=60)
    response.raise_for_status()
    response_json = response.json()
    print(f'Memory API response: {json.dumps(response_json, indent=2)}')
  except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')


@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}')
  print(f'Bot ID: {client.user.id}')
  print('------')


@client.event
async def on_message(message):
  global message_memory

  # Check if the message is from the bot or not in the desired channel
  if message.author == client.user or message.channel.name != 'ai-chat':
    return

  content = message.content.strip()

  if not content:
    print('Message content is empty after stripping.')
    return

  # filter for url links
  if content.startswith('http://') or content.startswith('https://'): 
    #upload_url(message.content)
    print(f'Message content: {message.content}' )
    #send discord message
    await message.channel.send(f'{message.author.mention} Your URL has been uploaded! Thank you!')
    return
  return 
  
  response, ai_score = get_ai_response(content)

  if not response:
    print('AI response is empty.')
    return

  await message.channel.send(f'{response} \nAI Score: {ai_score}')

  # Accumulate message details for memory
  message_details = f'Received message from {message.author.name}: {message.content}. AI response: {response}. AI Score: {ai_score}.'
  message_memory += message_details + "\n"

  # Check if the accumulated memory exceeds the character limit or the AI score is over +1
  if len(message_memory) > 64000 or ai_score > 1:
    upload_memory(message_memory, "Discord", "Discord Bot")
    message_memory = ""


client.run(bot_token)
