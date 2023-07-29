<!DOCTYPE html>
<html>
<head>
    <title>Your Bot's Name</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
        }

        h1 {
            color: #ff5a5f;
        }

        .logo {
            max-width: 200px;
            display: block;
            margin: 0 auto;
        }

        .commands {
            margin-top: 20px;
        }

        .command {
            margin-bottom: 10px;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }

        .command h2 {
            margin: 0;
            color: #ff5a5f;
        }

        .command p {
            margin: 0;
        }

        .footer {
            margin-top: 40px;
            color: #777;
        }
    </style>
</head>
<body>
    <h1>Your Bot's Name</h1>
    <img class="logo" src="link_to_your_bot_logo.png" alt="Bot Logo">

    <h2>Description</h2>
    <p>Your Bot's Name is a Discord bot that provides random memes and GIFs, and also allows users to participate in meme battles.</p>

    <h2>Installation</h2>
    <ol>
        <li>Clone this repository to your local machine.</li>
        <li>Install the required dependencies using pip:</li>
    </ol>
    <pre>pip install -r requirements.txt</pre>
    <ol start="3">
        <li>Create a new Discord bot on the <a href="https://discord.com/developers/applications">Discord Developer Portal</a>.</li>
        <li>Copy the bot token and paste it in the <code>config.py</code> file.</li>
        <li>Run the bot using the following command:</li>
    </ol>
    <pre>python index.py</pre>

    <h2>How to Use</h2>
    <div class="commands">
        <div class="command">
            <h2>!ping</h2>
            <p>Get the bot's latency.</p>
        </div>
        <div class="command">
            <h2>!meme</h2>
            <p>Get a random meme.</p>
        </div>
        <div class="command">
            <h2>!gif [query]</h2>
            <p>Search and get a GIF based on the query.</p>
        </div>
        <div class="command">
            <h2>!meme_battle</h2>
            <p>Participate in a meme battle with your own caption.</p>
        </div>
    </div>

    <h2>Contributing</h2>
    <p>If you'd like to contribute to Your Bot's Name, feel free to create a pull request with your changes. We welcome any improvements or new features!</p>

    <h2>License</h2>
    <p>Your Bot's Name is open-source and available under the <a href="link_to_license">MIT License</a>.</p>

    <h2>Acknowledgments</h2>
    <p>Special thanks to <a href="https://tenor.com/gifapi">Tenor</a> for providing the GIF API, and <a href="https://meme-api.com/">Meme API</a> for providing the meme API.</p>

    <div class="footer">
