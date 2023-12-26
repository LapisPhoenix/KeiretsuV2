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
- 📜 **Event Logging**: Logs certain events like message edits and deletions.


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
| botdebug        | Shows debug info about the bot                         | !botdebug                               | None    |
| reload          | Reloads a cog                                          | !reload [cog]                           | None    |
| shorten         | Shortens a URL                                         | !shorten [url]                          | None    |
| help_markdown   | Gives back the same response as help, but in markdown. | !help_markdown                          | None    |
| roll            | Rolls a dice                                           | !roll [max]                             | dice    |
| 8ball           | Ask the magic 8ball a question                         | !8ball [question]                       | None    |
| ping            | Pong!                                                  | !ping                                   | None    |
| unwatch         | Unwhitelists a channel for logging                     | !unwatch [channel]                      | None    |
| coinflip        | Flips a coin                                           | !coinflip                               | None    |
| mock            | Mocks a message                                        | !mock [message]                         | None    |
| bomb            | Message will detinate in 5 seconds                     | !bomb                                   | None    |
| loripsum        | Generates a random lorem ipsum                         | !loripsum [sentences] [sentence_length] | None    |
| guildinfo       | Shows debug info about the guild                       | !guildinfo [guild]                      | None    |
| help            | Shows this message                                     | !help                                   | None    |
| roleinfo        | Shows debug info about the role                        | !roleinfo [role]                        | None    |
| load            | Loads a cog                                            | !load [cog]                             | None    |
| unload          | Unloads a cog                                          | !unload [cog]                           | None    |
| watch           | Whitelists a channel for logging                       | !watch [channel]                        | None    |
| userinfo        | Shows debug info about the user                        | !userinfo [user]                        | None    |
| download        | Links to the github repo                               | !download                               | None    |
| channelinfo     | Shows debug info about the channel                     | !channelinfo [channel]                  | None    |
| emojiinfo       | Shows debug info about the emoji                       | !emojiinfo [emoji]                      | None    |
| shutdown        | Shuts down the bot                                     | !shutdown                               | None    |
| uptime          | Shows the bot's uptime                                 | !uptime                                 | None    |
| spotify         | Shows information about a spotify track                | !spotify                                | None    |
| pause           | Pauses the current spotify track                       | !spotify pause                          | None    |
| playlist_tracks | Shows the tracks of a spotify playlist                 | !spotify playlist_tracks [playlist]     | None    |
| status          | Shows the current spotify status                       | !spotify status                         | None    |
| categories      | Shows the available spotify categories                 | !spotify categories                     | None    |
| genres          | Shows the available spotify genres                     | !spotify genres                         | None    |
| next            | Plays the next spotify track                           | !spotify next                           | None    |
| artist          | Shows information about a spotify artist               | !spotify artist [artist]                | None    |
| track           | Shows information about a spotify track                | !spotify track [track]                  | None    |
| album           | Shows information about a spotify album                | !spotify album [album]                  | None    |
| recommend       | Recommends a spotify track                             | !spotify recommend [track]              | None    |
| previous        | Plays the previous spotify track                       | !spotify previous                       | None    |
| new             | Shows the new spotify releases                         | !spotify new                            | None    |
| playlist        | Shows information about a spotify playlist             | !spotify playlist [playlist]            | None    |
| resume          | Resumes the current spotify track                      | !spotify resume                         | None    |
| search          | Searches for a spotify track                           | !spotify search [query]                 | None    |
| featured        | Shows the featured spotify playlists                   | !spotify featured                       | None    |
| recent          | Shows the recent tracks of a spotify user              | !spotify recent [user]                  | None    |
| play            | Plays a spotify track                                  | !spotify play [track]                   | None    |
| related         | Shows related artists to a spotify artist              | !spotify related [artist]               | None    |
| category        | Shows the playlists of a spotify category              | !spotify category [category]            | None    |
| user            | Shows information about a spotify user                 | !spotify user [user]                    | None    |
| top             | Shows the top tracks of a spotify user                 | !spotify top [user]                     | None    |