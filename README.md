# Keiretsu V2

![Keiretsu V2 Logo](https://raw.githubusercontent.com/LapisPhoenix/KeiretsuV2/main/keiretsu_v2.png)

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
- 📜 ~~**Event Logging**: Logs certain events like message edits and deletions.~~ (Coming Soon)
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
| shorten         | Shortens a URL                                         | !shorten [url]                          | None    |
| reload          | Reloads a cog                                          | !reload [cog]                           | None    |
| empty           | Sends an empty message                                 | !empty                                  | None    |
| botdebug        | Shows debug info about the bot                         | !botdebug                               | None    |
| roleinfo        | Shows debug info about the role                        | !roleinfo [role]                        | None    |
| hexify          | Converts text to hex                                   | !hexify [message]                       | None    |
| shutdown        | Shuts down the bot                                     | !shutdown                               | None    |
| bomb            | Message will detinate in 5 seconds                     | !bomb                                   | None    |
| unmorse         | Converts morse code to text                            | !unmorse [message]                      | None    |
| ascii           | Converts text to ascii art                             | !ascii [message]                        | None    |
| clap            | Adds clap emojis between words                         | !clap [message]                         | None    |
| watch           | Whitelists a channel for logging                       | !watch [channel]                        | None    |
| roll            | Rolls a dice                                           | !roll [max]                             | dice    |
| coinflip        | Flips a coin                                           | !coinflip                               | None    |
| yt2mp4          | Converts a YouTube video to mp4                        | !yt2mp4 [url]                           | None    |
| help_markdown   | Gives back the same response as help, but in markdown. | !help_markdown                          | None    |
| morse           | Converts text to morse code                            | !morse [message]                        | None    |
| ping            | Pong!                                                  | !ping                                   | None    |
| unbinary        | Converts binary to text                                | !unbinary [message]                     | None    |
| loripsum        | Generates a random lorem ipsum                         | !loripsum [sentences] [sentence_length] | None    |
| count           | Counts down from n to x                                | !count [start] [end]                    | None    |
| unhexify        | Converts hex to text                                   | !unhexify [message]                     | None    |
| help            | Shows this message                                     | !help                                   | None    |
| emojiinfo       | Shows debug info about the emoji                       | !emojiinfo [emoji]                      | None    |
| binary          | Converts text to binary                                | !binary [message]                       | None    |
| 8ball           | Ask the magic 8ball a question                         | !8ball [question]                       | None    |
| channelinfo     | Shows debug info about the channel                     | !channelinfo [channel]                  | None    |
| download        | Links to the github repo                               | !download                               | None    |
| uptime          | Shows the bot's uptime                                 | !uptime                                 | None    |
| userinfo        | Shows debug info about the user                        | !userinfo [user]                        | None    |
| yt2mp3          | Converts a YouTube video to mp3                        | !yt2mp3 [url]                           | None    |
| load            | Loads a cog                                            | !load [cog]                             | None    |
| mock            | Mocks a message                                        | !mock [message]                         | None    |
| unwatch         | Unwhitelists a channel for logging                     | !unwatch [channel]                      | None    |
| guildinfo       | Shows debug info about the guild                       | !guildinfo [guild]                      | None    |
| spotify         | Shows information about a spotify track                | !spotify                                | None    |
| recommend       | Recommends a spotify track                             | !spotify recommend [track]              | None    |
| next            | Plays the next spotify track                           | !spotify next                           | None    |
| related         | Shows related artists to a spotify artist              | !spotify related [artist]               | None    |
| previous        | Plays the previous spotify track                       | !spotify previous                       | None    |
| pause           | Pauses the current spotify track                       | !spotify pause                          | None    |
| resume          | Resumes the current spotify track                      | !spotify resume                         | None    |
| play            | Plays a spotify track                                  | !spotify play [track]                   | None    |
| album           | Shows information about a spotify album                | !spotify album [album]                  | None    |
| categories      | Shows the available spotify categories                 | !spotify categories                     | None    |
| status          | Shows the current spotify status                       | !spotify status                         | None    |
| playlist        | Shows information about a spotify playlist             | !spotify playlist [playlist]            | None    |
| user            | Shows information about a spotify user                 | !spotify user [user]                    | None    |
| genres          | Shows the available spotify genres                     | !spotify genres                         | None    |
| track           | Shows information about a spotify track                | !spotify track [track]                  | None    |
| new             | Shows the new spotify releases                         | !spotify new                            | None    |
| recent          | Shows the recent tracks of a spotify user              | !spotify recent [user]                  | None    |
| playlist_tracks | Shows the tracks of a spotify playlist                 | !spotify playlist_tracks [playlist]     | None    |
| featured        | Shows the featured spotify playlists                   | !spotify featured                       | None    |
| artist          | Shows information about a spotify artist               | !spotify artist [artist]                | None    |
| top             | Shows the top tracks of a spotify user                 | !spotify top [user]                     | None    |
| category        | Shows the playlists of a spotify category              | !spotify category [category]            | None    |
| search          | Searches for a spotify track                           | !spotify search [query]                 | None    |
| unload          | Unloads a cog                                          | !unload [cog]                           | None    |
| charspoil       | Spoils a message character by character                | !charspoil [message]                    | None    |