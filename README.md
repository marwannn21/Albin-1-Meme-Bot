# Albin 1 - Simple Meme Bot Template

Albin 1 is a simple Discord bot template designed to create a meme bot for your Discord server. This template provides a basic setup for a bot that can fetch random memes and GIFs, participate in meme battles, and respond to pings. It serves as a starting point for anyone interested in building their own meme bot.

## Features

- Fetch random memes with `!meme`.
- Search for GIFs with `!gif [query]`.
- Participate in meme battles with `!meme_battle`.
- Get the bot's latency with `!ping`.

## Installation

To use this template and create your own meme bot, follow these steps:

1. Clone or download this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open the `index.py` file in a code editor.
4. Replace `YOUR_TOKEN_HERE` with your Discord bot token. You can obtain a bot token by creating a new bot on the [Discord Developer Portal](https://discord.com/developers/applications).
5. To enable GIF search functionality, you will need to get a GIPHY API key. Visit the [GIPHY Developers](https://developers.giphy.com/) website, sign up for an account, and create a new app to get the API key. Replace `YOUR_GIPHY_API_KEY` with your GIPHY API key in the `fetch_random_gif` function in the `commands.py` file.
6. Customize the bot's commands, add new features, or modify the behavior to suit your needs.

## How to Run

To run the bot, simply execute the `index.py` file using Python:
The bot will log in to Discord and be ready to use in the server where it was invited.

## Contributing

This bot template is open source, and contributions are welcome. If you have any improvements, bug fixes, or new features to add, feel free to submit a pull request. Please refer to the CONTRIBUTING.md file for more details on how to contribute.

## License

This bot template is released under the MIT License. You can find the full license in the LICENSE file.

## Acknowledgments

Special thanks to the Discord.py community and any external libraries or APIs used to build this template.

---

Please note that this template provides a basic setup for a simple meme bot. It's a starting point, and you can expand and customize it further to create a more advanced bot with additional features. Happy coding!
