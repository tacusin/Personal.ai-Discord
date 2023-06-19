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
5. Set up your secrets in the Secrets Panel:
   - `API_KEY` - API key for the AI service and memory API
   - `BOT_TOKEN` - Token for your Discord bot
   - `BASE_URL` - Base URL for the AI service API (Set it to 'https://api.personal.ai/v1/message')
   - `DOMAIN_NAME` - can be left blank for your main AI, or set up for a Sub-AI - ex. DomainName is "ai-climbing" for the profile URL of ai-climbing.personal.ai
   - `MEMORY_API_URL` - URL for the memory API (Set it to 'https://api.personal.ai/v1/memory')
6. Run the bot after setting discord.py as your entry point.

## Usage

1. Invite the bot to your Discord server using the provided OAuth2 link.
2. Start the bot by running the script.
3. The bot will listen to messages in the server channel named #ai-chat and respond accordingly.
4. Messages will be uploaded to the memory API for analysis.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

OPEN SOURCE 4 LIFE
