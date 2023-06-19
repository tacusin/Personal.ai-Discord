# Discord Bot

This Discord bot interacts with an AI service to generate responses and upload messages to a memory API. It is built using the Discord.py library.

## Features

- Chat with the bot and receive AI-generated responses.
- Messages are uploaded to a memory API for further analysis.

## Dependencies

- A Personal.ai API Tier Account
- A https://replit.com/ Account

## Installation

1. Navigate to [ReplIt](https://replit.com/~) home
2. Click the `Create Repl` Button
3. Click the `Import from GitHub` Button
4. In the URL box paste `https://github.com/tacusin/Personal.ai-Discord`
5. After it finishes importing set discord.py as your entry point and click done.
6. Set up your secrets in the Secrets Panel: They should import on their own but if they don't you can use the JSON as the end of this readme
   - `API_KEY` - API key for the AI service and memory API
   - `BOT_TOKEN` - Token for your Discord bot
   - `BASE_URL` - Base URL for the AI service API (Set it to 'https://api.personal.ai/v1/message')
   - `DOMAIN_NAME` - can be left blank for your main AI, or set up for a Sub-AI - ex. DomainName is "ai-climbing" for the profile URL of ai-climbing.personal.ai
   - `MEMORY_API_URL` - URL for the memory API (Set it to 'https://api.personal.ai/v1/memory')
7. Once you click RUN for the first time it should import and install all the dependencies needed for you.

## Usage

1. Invite the bot to your Discord server using the provided OAuth2 link.
2. Start the bot by running the script.
3. The bot will listen to messages in the server channel named #ai-chat and respond accordingly.
4. Messages will be uploaded to the memory API for analysis.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

OPEN SOURCE 4 LIFE

JSON for secrets:
```json
{
  "BASE_URL": "https://api.personal.ai/v1/message",
  "MEMORY_API_URL": "https://api.personal.ai/v1/memory",
  "API_KEY": "YOU PERSONAL AI API HERE",
  "BOT_TOKEN": "YOUR DISCORD BOT TOKEN HERE",
  "DOMAIN_NAME": " "
}
```
