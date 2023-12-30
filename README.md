# Keiretsu V2

![Keiretsu V2 Logo](https://raw.githubusercontent.com/LapisPhoenix/KeiretsuV2/main/assets/keiretsu_v2.png)

![Python Version](https://img.shields.io/badge/Python-3.12-yellow?logo=python&logoColor=white) ![Windows Supported True](https://img.shields.io/badge/Windows-Supported-green?logo=windows10) ![Linux Supported True](https://img.shields.io/badge/Linux-Supported-green?logo=linux?logoColor=white) ![MacOS Supported True](https://img.shields.io/badge/MacOS-Not_Supported-red?logo=apple?logoColor=white) ![License](https://img.shields.io/github/license/LapisPhoenix/KeiretsuV2?color=blue)



Keiretsu V2 is a Discord self-bot designed to be an all-in-one bot for your needs.

## 🚀 Features

- 🎲 **Fun Commands**: Includes commands like `8ball`, `coinflip`, `roll`, `bomb`, and `mock` for user entertainment.
- 🛠️ **Utility Commands**: Provides useful commands like `guildinfo`, `userinfo`, `channelinfo`, `roleinfo`, `emojiinfo`, and `ping`.
- 🎵 **Spotify Integration**: Allows users to play, pause, resume, and search for Spotify tracks, albums, and artists.
- 🎁 **Nitro Sniper**: Automatically attempts to redeem Discord Nitro codes found in messages.
- 🎉 **Giveaway Sniper**: Automatically reacts to giveaway messages to enter.
- 📝 **Markdown Generation**: Can generate markdown documentation for the bot.
- 🔄 **Cog Management**: Allows for reloading, unloading, and loading of cogs for easy bot management.
- 📈 **Detailed Debug Information**: Provides detailed debug information about the bot, guilds, users, channels, roles, and emojis.
- 🕹️ **Developer Tools**: Includes commands for developers to manage the bot.
- 📺 **YouTube Downloader**: Allows users to download YouTube videos as MP3s or MP4s.
- 👩‍💻 **Encryption**: Allows users to encrypt and decrypt messages. (Hex, Binary, Morse, etc.)


## 💻 Setup

1. Clone the repository.
2. Install the required Python packages using pip.
3. Set up your environment variables, including your Discord token. (Pro Tip: You can run `python geturtoken.py` to get a tutorial on how to get your token.)
4. Run `main.py` to start the bot.

## 📰 Contributing

Contributions are welcome! Please make sure to test your changes before submitting a pull request.

## © License

This project is licensed under the MIT License.


## 🔥 Full Command List
*Please note that Spotify commands require Spotify Premium to work.


**The prefix show, `!`, can be changed in your `.env` file.

| Command         | Description                                            | Usage                                   | Aliases |
|-----------------|--------------------------------------------------------|-----------------------------------------|---------|
| guildinfo       | Shows debug info about the guild                       | !guildinfo [guild]                      | None    |
| 8ball           | Ask the magic 8ball a question                         | !8ball [question]                       | None    |
| userinfo        | Shows debug info about the user                        | !userinfo [user]                        | None    |
| shutdown        | Shuts down the bot                                     | !shutdown                               | None    |
| coinflip        | Flips a coin                                           | !coinflip                               | None    |
| unbinary        | Converts binary to text                                | !unbinary [message]                     | None    |
| yt2mp4          | Converts a YouTube video to mp4                        | !yt2mp4 [url]                           | None    |
| roll            | Rolls a dice                                           | !roll [max]                             | dice    |
| mock            | Mocks a message                                        | !mock [message]                         | None    |
| 0=1             | Proves 0=1                                             | !0=1                                    | None    |
| yt2mp3          | Converts a YouTube video to mp3                        | !yt2mp3 [url]                           | None    |
| pi              | Gives back pi to the nth digit                         | !pi [digits]                            | None    |
| bomb            | Message will detinate in 5 seconds                     | !bomb                                   | None    |
| codeblock       | Sends a codeblock with the given language              | !codeblock                              | None    |
| html            | Sends a codeblock with the html language               | !codeblock html [code]                  | None    |
| rust            | Sends a codeblock with the rust language               | !codeblock rust [code]                  | None    |
| cpp             | Sends a codeblock with the cpp language                | !codeblock cpp [code]                   | None    |
| vb              | Sends a codeblock with the vb language                 | !codeblock vb [code]                    | None    |
| java            | Sends a codeblock with the java language               | !codeblock java [code]                  | None    |
| python          | Sends a codeblock with the python language             | !codeblock python [code]                | None    |
| sql             | Sends a codeblock with the sql language                | !codeblock sql [code]                   | None    |
| csharp          | Sends a codeblock with the csharp language             | !codeblock csharp [code]                | None    |
| xml             | Sends a codeblock with the xml language                | !codeblock xml [code]                   | None    |
| php             | Sends a codeblock with the php language                | !codeblock php [code]                   | None    |
| js              | Sends a codeblock with the javascript language         | !codeblock js [code]                    | None    |
| swift           | Sends a codeblock with the swift language              | !codeblock swift [code]                 | None    |
| css             | Sends a codeblock with the css language                | !codeblock css [code]                   | None    |
| yaml            | Sends a codeblock with the yaml language               | !codeblock yaml [code]                  | None    |
| ruby            | Sends a codeblock with the ruby language               | !codeblock ruby [code]                  | None    |
| c               | Sends a codeblock with the c language                  | !codeblock c [code]                     | None    |
| typescript      | Sends a codeblock with the typescript language         | !codeblock typescript [code]            | None    |
| morse           | Converts text to morse code                            | !morse [message]                        | None    |
| channelinfo     | Shows debug info about the channel                     | !channelinfo [channel]                  | None    |
| empty           | Sends an empty message                                 | !empty                                  | None    |
| roleinfo        | Shows debug info about the role                        | !roleinfo [role]                        | None    |
| charspoil       | Spoils a message character by character                | !charspoil [message]                    | None    |
| emojiinfo       | Shows debug info about the emoji                       | !emojiinfo [emoji]                      | None    |
| reload          | Reloads a cog                                          | !reload [cog]                           | None    |
| unmorse         | Converts morse code to text                            | !unmorse [message]                      | None    |
| shorten         | Shortens a URL                                         | !shorten [url]                          | None    |
| ping            | Pong!                                                  | !ping                                   | None    |
| clap            | Adds clap emojis between words                         | !clap [message]                         | None    |
| uptime          | Shows the bot's uptime                                 | !uptime                                 | None    |
| count           | Counts down from n to x                                | !count [start] [end]                    | None    |
| help            | Shows this message                                     | !help                                   | None    |
| help_markdown   | Gives back the same response as help, but in markdown. | !help_markdown                          | None    |
| unload          | Unloads a cog                                          | !unload [cog]                           | None    |
| download        | Links to the github repo                               | !download                               | None    |
| binary          | Converts text to binary                                | !binary [message]                       | None    |
| code            | Sends a codeblock with the given language              | !code [language] [code]                 | None    |
| botdebug        | Shows debug info about the bot                         | !botdebug                               | None    |
| ascii           | Converts text to ascii art                             | !ascii [message]                        | None    |
| hexify          | Converts text to hex                                   | !hexify [message]                       | None    |
| spotify         | Shows information about a spotify track                | !spotify                                | None    |
| status          | Shows the current spotify status                       | !spotify status                         | None    |
| artist          | Shows information about a spotify artist               | !spotify artist [artist]                | None    |
| playlist        | Shows information about a spotify playlist             | !spotify playlist [playlist]            | None    |
| user            | Shows information about a spotify user                 | !spotify user [user]                    | None    |
| search          | Searches for a spotify track                           | !spotify search [query]                 | None    | 
| top             | Shows the top tracks of a spotify user                 | !spotify top [user]                     | None    |
| recent          | Shows the recent tracks of a spotify user              | !spotify recent [user]                  | None    |
| recommend       | Recommends a spotify track                             | !spotify recommend [track]              | None    |
| related         | Shows related artists to a spotify artist              | !spotify related [artist]               | None    |
| play            | Plays a spotify track                                  | !spotify play [track]                   | None    |
| genres          | Shows the available spotify genres                     | !spotify genres                         | None    |
| pause           | Pauses the current spotify track                       | !spotify pause                          | None    |
| featured        | Shows the featured spotify playlists                   | !spotify featured                       | None    |
| resume          | Resumes the current spotify track                      | !spotify resume                         | None    |
| new             | Shows the new spotify releases                         | !spotify new                            | None    |
| next            | Plays the next spotify track                           | !spotify next                           | None    |
| categories      | Shows the available spotify categories                 | !spotify categories                     | None    |
| previous        | Plays the previous spotify track                       | !spotify previous                       | None    |
| category        | Shows the playlists of a spotify category              | !spotify category [category]            | None    |
| track           | Shows information about a spotify track                | !spotify track [track]                  | None    |
| playlist_tracks | Shows the tracks of a spotify playlist                 | !spotify playlist_tracks [playlist]     | None    |
| album           | Shows information about a spotify album                | !spotify album [album]                  | None    |
| load            | Loads a cog                                            | !load [cog]                             | None    |
| unhexify        | Converts hex to text                                   | !unhexify [message]                     | None    |
| loripsum        | Generates a random lorem ipsum                         | !loripsum [sentences] [sentence_length] | None    |
| unload          | Unloads a cog                                          | !unload [cog]                           | None    |
| charspoil       | Spoils a message character by character                | !charspoil [message]                    | None    |
